from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = ChatOpenAI()

class WorkoutRequest(BaseModel):
    target_muscle: list[str]
    weight_type: str
    fitness_level: str

class ExerciseFeature(BaseModel):
    exercise_name: str = Field(description="Name of the exercise")
    number_of_sets: str = Field(description="Sets x reps")
    how_to_perform: str = Field(description="How to perform this exercise (explanation)")
    key_form: str = Field(description="Key form cue")
    caution_tips: str = Field(description="Injury prevention tip")

base_prompt = PromptTemplate(
    input_variables=["target_muscle", "weight_type", "fitness_level"],
    template="""
You are a certified fitness trainer and exercise programming assistant.
Your job is to design safe, effective workouts based strictly on the user’s selections.
Only recommend exercises that match the chosen equipment and experience level.
Prioritize proper form cues and injury prevention.
Keep explanations clear and practical.

Create a workout plan using the following inputs:

Target muscle group: {target_muscle}
Available weight/equipment: {weight_type}
User fitness level: {fitness_level}

Rules:
1. If ONE muscle group is selected:
   - Focus on isolation + accessory exercises.

2. If MULTIPLE muscle groups are selected:
   - Prioritize compound exercises that train all selected muscles together.
   - Then add 1–2 accessory exercises if helpful.

3. Use ONLY the selected equipment.
4. Match difficulty to fitness level.
5. Always include form cues and injury prevention.
6. Suggest 4-5 exercises.

If any input combination is unsafe or unrealistic, suggest the closest safe alternative instead of refusing.
Do not invent equipment or levels not listed. Give me structured output in JSON format.
"""
)

class WorkoutResponse(BaseModel):
    exercises: list[ExerciseFeature]

@app.post('/json-generate')
def generate(data: WorkoutRequest):
    full_prompt = base_prompt.invoke({"target_muscle": data.target_muscle, "weight_type": data.weight_type, "fitness_level": data.fitness_level })
    structured_model = model.with_structured_output(WorkoutResponse, method='function_calling')
    result = structured_model.invoke(full_prompt)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
