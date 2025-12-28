import os
import google.generativeai as genai
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    print("GEMINI_API_KEY not found in environment variables. Please set it.")

app = FastAPI()

# Configure CORS
origins = [
    os.getenv("FRONTEND_URL", "http://localhost:3000"),  # Frontend URL for Docusaurus development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Physical AI & Humanoid Robotics Textbook Chatbot Backend!"}

from .api.router import api_router
app.include_router(api_router)
