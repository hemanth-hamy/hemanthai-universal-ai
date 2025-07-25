import streamlit as st
import pandas as pd
from utils.fixer_engine import diagnose_issue
from utils.log_viewer import load_logs, export_logs

st.set_page_config(page_title="Hemanth Oracle Fusion AI", layout="wide")

st.sidebar.image("assets/avatar.png", width=150)
st.sidebar.title("Hemanth Oracle Fusion AI")
tab = st.sidebar.radio("Choose Mode", ["Diagnose", "Logs"])

if tab == "Diagnose":
    st.header("🔍 Oracle Auto-Fix Diagnoser")
    input_text = st.text_area("Enter Oracle error, issue, or log excerpt:")
    if st.button("Diagnose"):
        if input_text.strip():
            result = diagnose_issue(input_text)
            st.success("AI Diagnosis:")
            st.markdown(result)
        else:
            st.warning("Please paste an error or description above.")

elif tab == "Logs":
    st.header("📊 System Log Viewer + Export")
    logs_df = load_logs()
    st.dataframe(logs_df, use_container_width=True)
    if st.button("📤 Export to CSV"):
        export_logs(logs_df)
        st.success("Logs exported as `diagnostic_logs.csv`.")
