# ============================== 
# UI_LOADING (USED VIA PAGE ROUTER)
# ==============================

import streamlit as st
from logic.logic_analyse import analyse
from logic.logic_reading import generate_structured_reading
import pandas as pd
import numpy as np

def show_loading():
    st.title("LOGOS is Revealing…")
    with st.spinner("Running full 7×7 heptagon analysis… This takes 30–90 seconds"):
        topic = st.session_state.topic
        result = analyse(topic)
        df = pd.DataFrame(result, index=st.session_state.get('layers', []), columns=st.session_state.get('planes', []))

        total_chars = sum(len(str(c)) for row in result for c in row)
        avg = total_chars / 49
        coherence = round(min(avg * 2.7, 99.99), 2)
        ratio = round(avg / 10, 3)

        reading = generate_structured_reading(topic, st.session_state.natural_sentence, coherence, ratio, df)
        full_reading = f"""LOGOS ANALYTICS FINDINGS
{'='*60}
Your question: {st.session_state.natural_sentence}
Interpreted as: {topic}
Date & time: {st.session_state.get('now', 'Now')}
Resonance Coherence: {coherence:.1f}%  │  Heptagonal Ratio: {ratio:.3f}/1.000

{reading}
"""

        st.session_state.df = df
        st.session_state.reading_text = full_reading
        st.session_state.coherence = coherence
        st.session_state.ratio = ratio
        st.rerun()