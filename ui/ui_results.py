# ==============================
# UI_RESULTS
# ==============================

import streamlit as st
import pandas as pd

def show_results():
    st.markdown(
        """
        <h1 style='text-align: center; margin-top: 80px;'>
            LOGOS Heptagon Results
        </h1>
        """,
        unsafe_allow_html=True
    )

    # Safety guard — if we somehow got here without data
    if 'df' not in st.session_state or st.session_state.df is None:
        st.error("No results yet — please go back and generate the heptagon.")
        if st.button("← Start Again"):
            st.session_state.clear()
            st.rerun()
        st.stop()

    # Use the original topic (we always have this)
    topic = st.session_state.get('topic', 'your topic')
    st.markdown(f"**Your question / topic:** {topic}", unsafe_allow_html=False)

    st.markdown("<h2 style='text-align: center;'>Your 7-sided analysis</h2>", unsafe_allow_html=True)

    # Placeholder until real heptagon is ready
    df = st.session_state.df
    st.dataframe(df, use_container_width=True)

    st.success("Heptagon generated successfully! (Real version coming very soon)")
    
    if st.button("Start New Analysis", type="primary"):
        st.session_state.clear()
        st.rerun()
