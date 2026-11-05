
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()
def pick_llm(level:str):
    """
    Picks the appropriate LLM based on the level of the question.

    Args:
        level (str): The level of the question, can be "low", "medium", or "high".

    Returns:
        ChatGoogleGenerativeAI: The LLM instance to be used.
    """
    level = level.lower()

    if level == "low":
        llm = ChatGoogleGenerativeAI(model= "gemini-3.1-flash-lite",temperature = 0)

    elif level == "mediem":
        llm = ChatGoogleGenerativeAI(model= "gemini-3.5-flash-lite",temperature = 0)
    elif level == "high":
        llm = ChatGoogleGenerativeAI(model= "gemini-3.6-flash",temperature = 0)

    else :
        raise ValueError(f"Unsupported level: {level}")
    return llm 

