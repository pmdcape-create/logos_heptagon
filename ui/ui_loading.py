# ============================== 
# UI_LOADING (USED VIA PAGE ROUTER)
# ==============================

import streamlit as st
import time

def show_loading():
    st.markdown(
        """
        <h1 style='text-align: center; margin-top: 100px;'>
            🔄 Processing Your Request
        </h1>
        """,
        unsafe_allow_html=True
    )

    # SAFETY FIRST – if topic is missing, send user back gracefully
    if 'topic' not in st.session_state or not st.session_state.topic:
        st.error("Oops! We lost your topic. Please start again.")
        if st.button("← Back to Questions"):
            st.session_state.topic_confirmed = False
            st.session_state.df = None
            st.rerun()
        st.stop()

    topic = st.session_state.topic

    st.markdown(f"<h2 style='text-align: center;'>“{topic}”</h2>", unsafe_allow_html=True)

    progress_bar = st.progress(0)
    status_text = st.empty()

    # Fake progress just for beauty (your real logic will replace this later)
    for i in range(100):
        time.sleep(0.03)
        progress_bar.progress(i + 1)
        status_text.text(f"Analysing {i+1}% complete...")

    # When done, store a dummy dataframe and go to results
    import pandas as pd
    dummy_data = pd.DataFrame({"Placeholder": ["Your real heptagon will appear here soon"]})
    st.session_state.df = dummy_data
    st.session_state.topic_confirmed = True
    progress_bar.empty()
    status_text.empty()
    st.rerun()
