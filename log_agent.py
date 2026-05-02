from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

def log_agent(state):
    query = state["query"].lower()
    module = state.get("module", "Unknown")

    # Rule-based hints (domain-aware)
    if "timeout" in query or "delay" in query:
        log_hint = "Possible timeout or network latency"
    elif "failed" in query or "error" in query:
        log_hint = "Application or transaction failure"
    elif "batch" in query:
        log_hint = "Batch processing issue"
    else:
        log_hint = "General system issue"

    prompt = f"""
    You are a banking production support expert.

    Issue: {query}
    Module: {module}

    Log Insight Hint: {log_hint}

    Tasks:
    1. Analyze likely log-level issues
    2. Identify possible technical causes
    3. Suggest what logs or checks should be performed

    Provide structured output.
    """
    try:
        response = llm.invoke(prompt).content
    except Exception as e:
        response = "Unable to perform log analysis."
    
    state["log_analysis"] = response
    state["log_hint"] = log_hint
    return state
