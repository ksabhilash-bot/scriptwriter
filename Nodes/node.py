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

def editor_node(state: PipelineState)->dict:
    """
    Clean Up grammar, removes typos, and improves the overall readability and refine tone of the text.
    """

    prompt = (
        "You are an expert copyeditor."
        "Your task is to clean up the grammar, remove typos, and improve the overall readability and refine the tone of the text.\n"
        "while keeping the core message intact. Return only the edited text.\n"
        f"Text:\n {state["raw_input"]}"
    )