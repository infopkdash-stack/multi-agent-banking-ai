from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

def diagnostic_agent(state):
    query = state["query"]

    prompt = f"""
    Identify the banking module (Payments, GL, LC, Loans) for this issue:
    {query}
    """

    response = llm.invoke(prompt).content
    state["diagnosis"] = response
    return state