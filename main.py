import os 
from dotenv import load_dotenv
from Nodes.EditorNode import editor_node
from Nodes.ScriptWriterNode import script_node
from Nodes.HinglishNode import Hinglish_node
from langgraph.graph import StateGraph,START,END
from state.state import PipelineState

graph = StateGraph(PipelineState)

#adding nodes in graph

graph.add_node("editor",editor_node)
graph.add_node("scriptwriter",script_node)
graph.add_node("hinglish",Hinglish_node)

#adding edges in graph sequential
graph.add_edge(START,"editor")
graph.add_edge("editor","scriptwriter")
graph.add_edge("scriptwriter","hinglish")
graph.add_edge("hinglish",END)

app=graph.compile() #compiled graph

result =app.invoke({"raw_input":"Ai agnets are the future of software development."})
print(result["final_output"])
