# ==============================
# UI_QUESTION
# ==============================

import streamlit as st
from logic.topic_extraction import extract_key_topics  # Assumes LLM call to get topics
from utils.api import get_llm_client

def show_question_flow():
    st.header("📝 Enter Your Question")
    
    question = st.text_area("Describe your real-life question or dilemma:", 
                            placeholder="E.g., 'Should I change careers at 40?'", 
                            height=100, max_chars=500)
    
    if question:
        if st.button("🔍 Extract Key Topics", type="secondary"):
            with st.spinner("Analyzing core aspects..."):
                client = get_llm_client()
                topics = extract_key_topics(client, question)  # Returns list like ["career-transition", "risk-assessment"]
                st.session_state.extracted_topics = topics
                st.session_state.question = question
        
        if 'extracted_topics' in st.session_state:
            topics_str = ", ".join(st.session_state.extracted_topics)
            st.markdown(f"**Detected Key Topics:** {topics_str}")
            st.markdown("*These underpin your question for accurate analysis.*")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ Verify & Proceed", type="primary"):
                    st.session_state.topic_confirmed = True
                    st.session_state.verified_topics = st.session_state.extracted_topics
                    st.rerun()
            with col2:
                if st.button("✏️ Edit Topics"):
                    new_topics = st.text_input("Enter revised topics (hyphen-joined phrases):", 
                                               placeholder="E.g., career-change-job-offer-personal-growth",
                                               value="-".join(st.session_state.extracted_topics))
                    if st.button("Update"):
                        edited = [t.strip() for t in new_topics.split("-") if t.strip()]
                        st.session_state.extracted_topics = edited
                        st.rerun()
    else:
        st.info("Enter a question to begin extraction.")
