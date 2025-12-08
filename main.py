# ==============================
# MAIN
# ==============================

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))        # Must be first!

# Now safe to import local modules
import streamlit as st
from ui.ui_welcome import show_welcome
from ui.ui_loading import show_loading
from ui.ui_question import show_question_flow
from ui.ui_results import show_results
from utils.api import setup_api_key, get_llm_client

# ============================== APP CONFIG ==============================
st.set_page_config(page_title="LOGOS Heptagon Revealer", layout="wide")

# ============================== SIDEBAR – API KEY ==============================
with st.sidebar:
    st.header("API Setup (Temporary)")
    api_key = setup_api_key()                     # Returns key or None

    if api_key:
        st.session_state.api_ready = True        # CRITICAL LINE
        st.success("API Key Loaded! Downloads Unlocked.")
        st.info("This is temporary. Future: Stripe integration.")
    else:
        st.session_state.api_ready = False
        st.warning("Enter your Grok API key to continue.")

# ============================== INITIALIZE SESSION STATE ONCE ==============================
if 'first_run' not in st.session_state:
    st.session_state.update({
        "first_run": True,
        "topic": "",
        "natural_sentence": "",
        "topic_confirmed": False,
        "df": None,
        "reading_text": "",
        "coherence": 0.0,
        "ratio": 0.0,
        "api_ready": False,           # will be overridden by sidebar above
    })

# ============================== MAIN FLOW ==============================
if st.session_state.first_run:
    show_welcome()
    st.session_state.first_run = False                    # only runs once

else:
    # User has passed the welcome screen
    if not st.session_state.api_ready:
        st.warning("Please set up your API key in the sidebar to proceed.")
        st.stop()                                          # blocks everything below

    # Normal flow
    if st.session_state.get("df") is not None:
        show_results()
    elif st.session_state.get("topic_confirmed"):
        show_loading()
    else:
        show_question_flow()
