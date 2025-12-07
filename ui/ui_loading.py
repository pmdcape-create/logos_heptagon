# ============================== 
# UI_LOADING (USED VIA PAGE ROUTER)
# ==============================


import streamlit as st
import time
from logic.analysis import run_full_analysis  # Assumes this computes df, summary, scores
from utils.api import get_llm_client

def show_loading():
    st.header("⚡ Computing Resonances")
    with st.spinner("Running full 7×7 analysis across 49 layers... (30-90s)"):
        client = get_llm_client()
        question = st.session_state.question
        topics = st.session_state.verified_topics
        df, summary_text, coherence_score, ratio = run_full_analysis(client, question, topics)
        st.session_state.df = df
        st.session_state.summary_text = summary_text
        st.session_state.coherence_score = coherence_score
        st.session_state.ratio = ratio
        time.sleep(1)  # Brief pause for effect
        st.success("Analysis Complete!")
        st.rerun()
