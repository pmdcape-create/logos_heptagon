# ==============================
# UI_QUESTION
# ==============================

import streamlit as st

def show_question_flow():
    st.markdown(
        """
        <h1 style='text-align: center; margin-top: 100px;'>
            What would you like to explore today?
        </h1>
        """,
        unsafe_allow_html=True
    )

    # Input box
    topic_input = st.text_input(
        "",
        placeholder="Type your topic or question here and press Enter ↵",
        label_visibility="collapsed",
        key="topic_input_key"
    )

    # When user presses Enter or submits
    if topic_input:
        # ←←← THIS IS THE CRUCIAL PART THAT WAS MISSING BEFORE
        st.session_state.topic = topic_input.strip()
        st.session_state.topic_confirmed = True
        st.session_state.first_run = False
        st.rerun()

    # Optional: nice centered button as backup
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Generate LOGOS Heptagon →", type="primary", use_container_width=True):
            if topic_input:
                st.session_state.topic = topic_input.strip()
                st.session_state.topic_confirmed = True
                st.session_state.first_run = False
                st.rerun()
            else:
                st.warning("Please type something first")
