from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

def resolution_agent(state):
    context = state.get("context", "")

    prompt = f"""
    Based on context: {context}
    Provide root cause and resolution steps.
    """

    response = llm.invoke(prompt).content
    state["resolution"] = response
    return state