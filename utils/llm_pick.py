
from langchain_groq import ChatGroq
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
        llm = ChatGroq(model= "openai/gpt-oss-20b",temperature = 0)

    elif level == "medium":
        
        llm = ChatGroq(model= "openai/gpt-oss-120b",temperature = 0)
    elif level == "high":
        llm = ChatGroq(model= "qwen/qwen3.8-27b",temperature = 0)

    else :
        raise ValueError(f"Unsupported level: {level}")
    return llm 

