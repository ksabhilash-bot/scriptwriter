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

def editor_node(state: PipelineState)->dict:
    """
    Clean Up grammar, removes typos, and improves the overall readability and refine tone of the text.
    """

    prompt = (
        "You are an expert copyeditor."
        "Your task is to clean up the grammar, remove typos, and improve the overall readability and refine the tone of the text.\n"
        "while keeping the core message intact. Return only the edited text.\n"
        f"Text:\n {state['raw_input']}"
    )

    response = llm.invoke(prompt)

    return {"edited_text":response.content.strip()}