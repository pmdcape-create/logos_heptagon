# ============================== 
# UI_LOADING (USED VIA PAGE ROUTER)
# ==============================


import streamlit as st
import time

from logic.analysis import run_full_analysis
from utils.api import get_llm_client   # ← add this line

def show_loading():
    st.header("⚡ Computing Resonances")
    with st.spinner("Running full 7×7 analysis across 49 layers... (30-90s)"):
        client = get_llm_client()
        question = st.session_state.question
        topics = st.session_state.verified_topics
        # Get the client (this is how the new engine expects it)
        client = get_llm_client()

        # Now run the real sacred analysis
        df, summary, coherence, ratio = run_full_analysis(client, question, topics)
        
        st.session_state.df = df
        st.session_state.summary_text = summary_text
        st.session_state.coherence_score = coherence_score
        st.session_state.ratio = ratio
        time.sleep(1)  # Brief pause for effect
        st.success("Analysis Complete!")
        st.rerun()
