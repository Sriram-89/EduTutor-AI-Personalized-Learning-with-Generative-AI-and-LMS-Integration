from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to EduTutor AI Backend"}

@app.post("/generate-quiz/")
async def generate_quiz(request: Request):
    data = await request.json()
    topic = data.get("topic")
    difficulty = data.get("difficulty")

    # Example question (you can add more logic to generate real questions)
    questions = [
        {"question": f"What is {topic}?", "options": ["A", "B", "C", "D"], "answer": "A"}
    ]

    return {"quiz": questions}