from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()  # .env file se keys load karta hai

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

app = FastAPI(
    title="Langchain Routing Spec",
    version="1.0.0",
    description="A routing platform for connecting the LLM",
)

# Dono models
gemini_model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
groq_model = ChatGroq(model_name="openai/gpt-oss-20b")

# Prompts: {topic} jagah user ka sawal aayega
prompt_tech = ChatPromptTemplate.from_template("Please tell me what is {topic}")
prompt_nontech = ChatPromptTemplate.from_template("Please tell me what is {topic}")

# Routes: har chain ek endpoint ban jaata hai
add_routes(app, prompt_tech | gemini_model, path="/gemini/tech")
add_routes(app, prompt_nontech | groq_model, path="/groq/nontech")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)