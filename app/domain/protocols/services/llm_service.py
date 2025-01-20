# Your LLM Service Protocol here
from langchain_openai import ChatOpenAI
import os

def model():
    API_KEY=os.getenv("OPENAI_API_KEY")
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=API_KEY,
    )
    return llm