from langchain_google_genai import ChatGoogleGenerativeAI
from state.state import PipelineState
from dotenv import load_dotenv
import os
load_dotenv()

api_key= os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    google_api_key=api_key,
    model = "gemini-2.5-flash",
    temperature=0.7,
)


def script_node(state: PipelineState)->dict:
    """
    Write a script based on the provided input.
    """

    prompt = (
        "You are an expert Youtube content creator."
        "Your task is to take this edited text and transform it into highly enggaging , punchy, converstaional video script hook.\n"
        "make it sound like a real person speaking passionately.Return only the script content.\n"
        f"Input:\n {state['edited_text']}"
    )

    response = llm.invoke(prompt)

    return {"script_text":response.content.strip()}