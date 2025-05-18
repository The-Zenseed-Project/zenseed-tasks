from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/tasks")
def get_tasks():
    return [
        {"id": 1, "title": "Write MVP plan", "completed": False},
        {"id": 2, "title": "Test TTS mode", "completed": False},
        {"id": 3, "title": "Invite contributors", "completed": True},
    ]
