import os
import re
import streamlit as st
import requests
from dotenv import load_dotenv
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.utils import simpleSplit

# Load API key
load_dotenv()
API_URL = "https://router.huggingface.co/hyperbolic/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {os.getenv('HF_API_KEY')}",
}


# Cleaned, non-streaming query function
def query_deepseek(messages):
    payload = {
        "messages": messages,
        "model": "deepseek-ai/DeepSeek-R1"
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        raw_reply = response.json()["choices"][0]["message"]["content"]
        clean_reply = re.sub(r"<think>.*?</think>", "", raw_reply, flags=re.DOTALL).strip()
        return clean_reply
    else:
        return f"Error: {response.status_code} - {response.text}"

def generate_chat_pdf(chat_history):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    c.setTitle("FitBuddy AI - Your Custom Fitness Plan")

    # Initial layout settings
    y = height - 50
    line_height = 18
    margin = 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(margin, y, "FitBuddy AI - Your Fitness Chat Summary")
    y -= 30

    c.setFont("Helvetica", 11)

    for msg in chat_history[1:]:  # Skip system prompt
        role = msg["role"].capitalize()
        content_lines = msg["content"].split("\n")

        if y < 100:
            c.showPage()
            y = height - 50
            c.setFont("Helvetica", 11)

        c.setFont("Helvetica-Bold", 12)
        c.drawString(margin, y, f"{role}:")
        y -= line_height

        c.setFont("Helvetica", 11)

        for line in content_lines:
            line = line.strip()

            if not line:
                y -= line_height // 2
                continue

            if y < 70:
                c.showPage()
                y = height - 50
                c.setFont("Helvetica", 11)

            # Markdown bold headers: **Header**
            if re.match(r"\*\*(.+?)\*\*", line):
                header = re.sub(r"\*\*(.+?)\*\*", r"\1", line)
                c.setFont("Helvetica-Bold", 11)
                c.drawString(margin, y, header)
                y -= line_height
                continue

            # Section divider
            if line.startswith("---") or line.startswith("—"):
                c.drawString(margin, y, "-" * 80)
                y -= line_height
                continue

            # Pattern: - Label: Content
            bullet_match = re.match(r"-\s*([^:]+):\s*(.*)", line)
            if bullet_match:
                label = bullet_match.group(1).strip()
                desc = bullet_match.group(2).strip()

                c.setFont("Helvetica-Bold", 11)
                c.drawString(margin, y, f"• {label}:")
                y -= line_height

                if desc:
                    wrapped = simpleSplit(desc, "Helvetica", 11, width - margin * 2)
                    c.setFont("Helvetica", 11)
                    for wline in wrapped:
                        c.drawString(margin + 20, y, wline)
                        y -= line_height
                continue

            # Simple bullet: - Something
            if line.startswith("- "):
                text = line[2:]
                wrapped = simpleSplit(text, "Helvetica", 11, width - margin * 2)
                for wline in wrapped:
                    c.drawString(margin + 10, y, f"• {wline}")
                    y -= line_height
                continue

            # Colon-based key-value line
            if ":" in line and not line.startswith("http"):
                key, val = line.split(":", 1)
                c.setFont("Helvetica-Bold", 11)
                c.drawString(margin, y, f"{key.strip()}:")
                y -= line_height
                c.setFont("Helvetica", 11)
                wrapped = simpleSplit(val.strip(), "Helvetica", 11, width - margin * 2)
                for wline in wrapped:
                    c.drawString(margin + 20, y, wline)
                    y -= line_height
                continue

            # Default fallback
            wrapped = simpleSplit(line, "Helvetica", 11, width - margin * 2)
            for wline in wrapped:
                c.drawString(margin, y, wline)
                y -= line_height

        y -= 10  # spacing between chats

    c.save()
    buffer.seek(0)
    return buffer

# Streamlit UI Setup
st.set_page_config(page_title="FitBuddy AI", layout="wide", page_icon="🏋️")
st.title("🏋️ FitBuddy AI - Your Gym & Nutrition Chatbot")

# Initialize chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "system",
            "content": (
                "You are FitBuddy AI, a helpful fitness assistant who gives friendly and knowledgeable advice "
                "on gym workouts, training splits, muscle recovery, diet plans, nutrition, supplements, sleep habits, "
                "and healthy lifestyle choices. Keep your responses concise, motivating, and based on scientific principles "
                "or commonly accepted fitness practices."
            )
        }
    ]

# Show previous chat
for msg in st.session_state.chat_history[1:]:
    st.chat_message(msg["role"]).markdown(msg["content"])

# User input
user_input = st.chat_input("Ask me anything about gym, food, or fitness...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.spinner("Preparing your personalized solution my friend..."):
        reply = query_deepseek(st.session_state.chat_history)

    st.chat_message("assistant").markdown(reply)
    st.session_state.chat_history.append({"role": "assistant", "content": reply})

# PDF download button
if len(st.session_state.chat_history) > 1:  # means at least one user message exists
    pdf_buffer = generate_chat_pdf(st.session_state.chat_history)
    st.download_button(
        label="📥 Download This Plan as PDF",
        data=pdf_buffer,
        file_name="FitBuddy_Chat_Plan.pdf",
        mime="application/pdf"
    )
