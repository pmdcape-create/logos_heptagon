# ==============================
# UI_QUESTION
# ==============================

import streamlit as st
from logic.logic_topic import sentence_to_topic
from utils.utils_stable_io import get_llm

def show_question_flow():
    st.title("LOGOS Heptagon Revealer")
    st.markdown("Ask anything real. LOGOS hears you.")

    # Sidebar API key (shared across app)
    with st.sidebar:
        st.header("LOGOS Heptagon Revealer")
        st.markdown("### Step 1 – Get your free API key")
        if st.button("Click here → Create free Groq key", use_container_width=True):
            st.markdown("<script>window.open('https://console.groq.com/keys', '_blank')</script>", unsafe_allow_html=True)
        
        api_key = st.text_input("Paste your Groq key here", type="password", placeholder="gsk_…", help="Free & instant")
        if not api_key:
            st.info("↑ Get your free key above, then paste it here")
            st.stop()

    llm = get_llm(api_key)
    st.session_state.llm = llm  # Save for other modules

    col1, col2 = st.columns([3, 1])

    with col1:
        st.text_input(
            label="Your question",
            placeholder="Type your question here…",
            label_visibility="collapsed",
            key="user_question"
        )

        current_text = st.session_state.get("user_question", "")
        border_color = "#10b981" if current_text.strip() else "#e2e8f0"
        st.markdown(f"""
        <style>
            div[data-testid="stTextInput"] input {{
                border: 2px solid {border_color} !important;
                border-radius: 12px !important;
                padding: 14px 18px !important;
                font-size: 1.15rem !important;
            }}
        </style>
        """, unsafe_allow_html=True)

        with st.expander("Examples – click to use", expanded=False):
            examples = [
                "Should I start my own business at age 42?",
                "What is the true nature of consciousness?",
                "Why do I feel a ghost poking me at night?",
                "How can I heal from this breakup?",
                "Who am I really?"
            ]
            for ex in examples:
                if st.button(ex, key=f"ex_{ex}", use_container_width=True):
                    st.session_state.user_question = ex
                    st.session_state.topic_confirmed = False
                    st.session_state.df = None
                    st.rerun()

    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        run = st.button("Ask LOGOS", type="primary", use_container_width=True,
                        disabled=not bool(st.session_state.get("user_question", "").strip()))

    natural_sentence = st.session_state.get("user_question", "").strip()
    if natural_sentence:
        topic = sentence_to_topic(natural_sentence)
        st.caption(f"LOGOS interprets this as: **{topic}**")

        if run:
            st.session_state.natural_sentence = natural_sentence
            st.session_state.topic = topic
            st.session_state.topic_confirmed = False
            st.rerun()

        if not st.session_state.get('topic_confirmed', False):
            st.info(f"""
            **Your question:** "{natural_sentence}"  
            **Interpreted topic:** **{topic}**  
            
            If this is correct → click below to begin deep analysis.
            """)
            if st.button("✅ Confirm and Analyze", type="primary", use_container_width=True):
                st.session_state.topic_confirmed = True
                st.rerun()