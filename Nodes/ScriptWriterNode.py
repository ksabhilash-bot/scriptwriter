from langchain_xai import ChatXAI
from state.state import PipelineState
from dotenv import load_dotenv
import os
load_dotenv()

api_key= os.getenv("XAI_API_KEY")

llm = ChatXAI(
    xai_api_key=api_key,
    model = "grok-4",
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
        f"Input:\n {state["edited_text"]}"
    )

    response = llm.invoke(prompt)

    return {"script_text":response.content.strip()}