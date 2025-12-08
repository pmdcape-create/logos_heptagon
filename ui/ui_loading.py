# ui/ui_loading.py

import streamlit as st
from utils.api import get_llm_client
from logic.analysis import run_full_analysis   # ← fixed import

def show_loading():
    if not st.session_state.get("topic_confirmed"):
        return

    st.write("### Running sacred LOGOS 7×7 analysis…")
    st.write("This takes 30–60 seconds. Please wait — every cell is being revealed individually.")

    # Get fresh client and run the real engine
    client = get_llm_client()
    
    # Run the full sacred analysis
    df, summary, coherence, ratio = run_full_analysis(client, st.session_state.natural_sentence, [])

    # Save everything to session state
    st.session_state.df = df
    st.session_state.reading_text = summary
    st.session_state.coherence = coherence
    st.session_state.ratio = ratio
    st.session_state.topic_confirmed = True

    st.success("Analysis complete!")
    st.rerun()
