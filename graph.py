from langgraph.graph import StateGraph
from diagnostic_agent import diagnostic_agent
from log_agent import log_agent
from resolution_agent import resolution_agent
from Rag import create_vector_store

db = create_vector_store()

def rag_step(state):
    query = state["query"]
    docs = db.similarity_search(query)
    state["context"] = " ".join([d.page_content for d in docs])
    return state

def build_graph():
    graph = StateGraph(dict)

    graph.add_node("diagnostic", diagnostic_agent)
    graph.add_node("log_analysis", log_agent)
    graph.add_node("rag", rag_step)
    graph.add_node("resolution", resolution_agent)

    graph.set_entry_point("diagnostic")
    graph.add_edge("diagnostic", "log_analysis")
    graph.add_edge("log_analysis", "rag")
    graph.add_edge("rag", "resolution")

    return graph.compile()