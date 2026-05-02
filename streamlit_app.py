import streamlit as st
import config  # Ensures env variables are loaded
from graph import build_graph

st.title("🏦 AI Banking Support Assistant")

query = st.text_input("Enter Issue:")

if st.button("Analyze"):
    with st.spinner("Analyzing..."):
        graph = build_graph()
        result = graph.invoke({"query": query})

        st.subheader("Diagnosis")
        st.write(result.get("diagnosis"))

        st.subheader("Log Insight")
        st.write(result.get("log_hint"))

        st.subheader("Log Analysis")
        st.write(result.get("log_analysis"))

        st.subheader("Resolution")
        st.write(result.get("resolution"))

        st.subheader("Resolution Confidence")
        st.write(result.get("resolution_confidence"))
