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


def Hinglish_node(state: PipelineState)->dict:
    """
    Convert the text to Hinglish, maintaining the core message while adding a colloquial touch.
    """

    prompt = (
        "You are an expert content localizer for the indian market.take the following script and convert it into natural, flowing 'hinglish'.\n"
        "Your task is to maintain the core message while adding a colloquial touch. Return only the converted text.\n"
        f"Text:\n {state['raw_input']}"
    )

    response = llm.invoke(prompt)

    return {"final_output":response.content.strip()}