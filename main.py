# ==============================
# MAIN
# ==============================

# ============================== # MAIN # ==============================
import streamlit as st
from ui.ui_welcome import show_welcome
from ui.ui_loading import show_loading
from ui.ui_question import show_question_flow
from ui.ui_results import show_results
from utils.api import setup_api_key, get_llm_client  # For API sidebar
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))   # ← THIS LINE FIXES EVERYTHING

# ============================== # APP ENTRY POINT # ==============================
st.set_page_config(page_title="LOGOS Heptagon Revealer", layout="wide")

# Sidebar: Temporary API Key Setup (hidden downloads until valid)
with st.sidebar:
    st.header("🔑 API Setup (Temporary)")
    api_key = setup_api_key()  # Handles input, validation, visibility toggle
    if api_key:
        st.success("API Key Loaded! Downloads Unlocked.")
        st.info("💡 This is temporary. Future: Replace with payment gateway (e.g., Stripe).")
    else:
        st.warning("Enter API key to enable downloads.")

# Initialize session state
if 'first_run' not in st.session_state:
    st.session_state.first_run = True
    st.session_state.api_ready = bool(api_key)
    st.session_state.topic_confirmed = False
    st.session_state.df = None
    st.session_state.summary_text = None
    st.session_state.coherence_score = None
    st.session_state.ratio = None

if st.session_state.get('first_run', False):
    show_welcome()
    st.session_state.first_run = False
else:
    # Main flow after welcome
    if not st.session_state.api_ready:
        st.warning("Please set up your API key in the sidebar to proceed.")
    elif st.session_state.get('topic_confirmed') and st.session_state.get('df') is None:
        show_loading()
    elif st.session_state.get('df') is not None:
        show_results()
    else:
        show_question_flow()
