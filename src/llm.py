import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def load_llm():
    return ChatOpenAI(
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1",
        model_name="moonshotai/kimi-dev-72b:free",
        temperature=0.8
    )
