# 🏋️ FitBuddy AI - Your Gym & Nutrition Chatbot

**FitBuddy AI** is a personalized fitness chatbot built using **Streamlit** and powered by **DeepSeek via Hugging Face API**. It’s designed to act like your virtual gym bro — guiding users on workout splits, diet, supplements, and recovery using a friendly tone and structured markdown formatting.

---

## 🚀 Features

- 🤖 Chat with a gym-savvy AI powered by DeepSeek-R1
- 📄 Generate a downloadable PDF of your full chat conversation
- 🧾 Clean markdown formatting in both UI and PDF

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** (frontend)
- **DeepSeek-R1 via Hugging Face API**
- **ReportLab** (PDF generation)
- **dotenv** (environment variable handling)

---

## 📂 Project Structure

```
fitbuddy-ai/
├── app.py                  # Main Streamlit app with pdf generation
├── .env                    # API key (not pushed to GitHub)
├── requirements.txt        # Python dependencies
└── README.md               # Project readme
```

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/fitbuddy-ai.git
cd fitbuddy-ai
```

### 2. Set up virtual environment

```bash
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Hugging Face API key

Create a `.env` file:

```
HF_API_KEY=your_huggingface_api_key_here
```

### 5. Run the app

```bash
streamlit run app.py
```

---

## 📄 Export to PDF

Click the **"📥 Download This Plan as PDF"** button after your conversation. This generates a PDF of the entire chat history (excluding the system prompt) with markdown-style formatting.

---

## 🧠 Future Add-ons

- 🔒 Persistent history with SQLite or Firebase
- 📊 Progress tracker & habit scoring
- 🗣️ Voice assistant integration

---

## 📌 API Details

- **Endpoint**: `https://router.huggingface.co/hyperbolic/v1/chat/completions`
- **Model**: `deepseek-ai/DeepSeek-R1`
- **Streaming**: Disabled (final response only)
- **Auth**: Requires Bearer token via `.env`

---

## 🙌 Acknowledgements

- [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1)
- [Streamlit](https://streamlit.io/)
- [ReportLab PDF](https://www.reportlab.com/)
- [Hugging Face Inference Endpoints](https://huggingface.co/docs/inference-endpoints/index)

---

### Built by Ronit Murpani
