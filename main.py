# ==============================
# main.py  – FINAL POLISHED VERSION
# ==============================

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

import streamlit as st
from ui.ui_welcome import show_welcome
from ui.ui_loading import show_loading
from ui.ui_question import show_question_flow
from ui.ui_results import show_results
from utils.api import setup_api_key

# ============================== CONFIG ==============================
st.set_page_config(page_title="LOGOS Heptagon Revealer", layout="wide")

# ============================== SIDEBAR ==============================
with st.sidebar:
    st.header("API Setup")
    api_key = setup_api_key()
    if api_key:
        st.session_state.api_ready = True
        st.success("API key valid – ready!")
    else:
        st.session_state.api_ready = False

# ============================== SESSION STATE (once only) ==============================
if "first_run" not in st.session_state:
    st.session_state.update({
        "first_run": True,
        "topic": "", "natural_sentence": "", "topic_confirmed": False,
        "df": None, "reading_text": "", "coherence": 0.0, "ratio": 0.0,
        "api_ready": False,
    })

# ============================== MAIN FLOW ==============================
if st.session_state.first_run:
    show_welcome()
    st.session_state.first_run = False

else:
    if not st.session_state.api_ready:
        st.warning("Please enter your Grok API key in the sidebar first.")
        st.stop()

    if st.session_state.get("df") is not None:
        show_results()                      # ← now has Summary → Grid → Buttons
    elif st.session_state.get("topic_confirmed"):
        show_loading()
    else:
        show_question_flow()
