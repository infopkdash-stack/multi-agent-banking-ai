from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

def log_agent(state):
    query = state["query"]

    prompt = f"""
    Analyze possible log issues for:
    {query}
    """

    response = llm.invoke(prompt).content
    state["log_analysis"] = response
    return state