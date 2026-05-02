from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

def resolution_agent(state):
    query = state["query"]
    module = state.get("module", "Unknown")
    context = state.get("context", "")
    log_analysis = state.get("log_analysis", "")

    prompt = f"""
    You are a senior banking production support engineer.

    Issue: {query}
    Module: {module}

    Log Analysis:
    {log_analysis}

    Historical Context (RAG):
    {context}

    Tasks:
    1. Identify root cause
    2. Provide step-by-step resolution
    3. Suggest preventive measures

    Keep response clear and actionable.
    """
    try:
        response = llm.invoke(prompt).content
    except Exception as e:
        response = "Unable to generate resolution."

    # Optional: basic confidence logic
    if module == "Unknown":
        confidence = "Low"
    else:
        confidence = "Medium"

    # Update state
    state["resolution"] = response
    state["resolution_confidence"] = confidence
    return state
