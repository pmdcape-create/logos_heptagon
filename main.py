# ==============================
# MAIN
# ==============================

import streamlit as st
from ui.ui_welcome import show_welcome
from ui.ui_loading import show_loading
from ui.ui_question import show_question_flow
from ui.ui_results import show_results

# ==============================
# APP ENTRY POINT
# ==============================

st.set_page_config(page_title="LOGOS", layout="wide")

# First run: show welcome screen
if 'first_run' not in st.session_state:
    st.session_state.first_run = True

if st.session_state.get('first_run', False):
    show_welcome()
else:
    # Main flow after welcome
    if st.session_state.get('topic_confirmed') and st.session_state.get('df') is None:
        show_loading()
    elif st.session_state.get('df') is not None:
        show_results()
    else:
        show_question_flow()