# ============================== 
# UI_LOADING (USED VIA PAGE ROUTER)
# ==============================

import streamlit as st
import time

def show_loading():
    st.markdown("<h1 style='text-align: center; margin-top: 80px;'>Building Your LOGOS Heptagon</h1>", 
                unsafe_allow_html=True)

    if 'topic' not in st.session_state or not st.session_state.topic:
        st.error("Oops! Topic missing.")
        if st.button("Back"):
            st.session_state.topic_confirmed = False
            st.rerun()
        st.stop()

    topic = st.session_state.topic
    st.markdown(f"<h2 style='text-align: center; color: #555;'>“{topic}”</h2>", unsafe_allow_html=True)

    progress_bar = st.progress(0)
    status = st.empty()
    detail = st.empty()

    steps = [
        "Initializing quantum coherence engine...",
        "Mapping semantic vectors across 7 axes...",
        "Aligning philosophical archetypes...",
        "Calculating tension fields...",
        "Resolving paradoxes...",
        "Rendering heptagonal symmetry...",
        "Finalizing insight matrix..."
    ]

    for i in range(100):
        time.sleep(0.08)  # Feels like real work
        progress_bar.progress(i + 1)
        step_idx = min(i // 15, len(steps) - 1)
        status.markdown(f"**{steps[step_idx]}**")
        detail.markdown(f"Progress: {i+1}%")

    # Create slightly more realistic dummy data
    import pandas as pd
    data = {
        "Dimension": ["Thesis", "Antithesis", "Synthesis", "Paradox", "Transcendence", "Ground", "Horizon"],
        "Insight": [
            "Clear emergence of core pattern",
            "Strong counter-force detected",
            "Integration zone identified",
            "Creative tension at peak",
            "Breakthrough window opening",
            "Stable foundation confirmed",
            "Future trajectory projected"
        ],
        "Strength": [88, 76, 91, 64, 82, 95, 79]
    }
    st.session_state.df = pd.DataFrame(data)
    st.session_state.analysis_complete = True

    progress_bar.empty()
    status.empty()
    detail.empty()
    st.success("Heptagon successfully generated!")
    time.sleep(1)
    st.rerun()
