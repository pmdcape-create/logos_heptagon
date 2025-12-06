# ==============================
# UI_RESULTS
# ==============================

import streamlit as st
from utils.utils_stable_io import reading_to_pdf, grid_to_html

def show_results():
    st.success("LOGOS analysis complete")
    st.markdown(f"**Your question:** {st.session_state.natural_sentence}")
    st.markdown(f"**Coherence:** {st.session_state.coherence:.1f}%  │ **Ratio:** {st.session_state.ratio:.3f}/1.000")

    st.subheader("LOGOS FINDINGS & INTERPRETATION")
    st.markdown(st.session_state.reading_text)

    st.markdown("---")
    st.subheader("7×7 Heptagon Data Grid")
    st.dataframe(st.session_state.df.style.set_properties(**{'text-align': 'left', 'white-space': 'pre-wrap'}),
                 use_container_width=True)

    c1, c2 = st.columns(2)
    with c1:
        st.download_button(
            "Download 7×7 Grid (HTML)",
            grid_to_html(st.session_state.df, st.session_state.topic, st.session_state.coherence, st.session_state.ratio).getvalue(),
            f"LOGOS_Grid_{st.session_state.topic}.html",
            "text/html"
        )
    with c2:
        st.download_button(
            "Download Findings (PDF)",
            reading_to_pdf(st.session_state.reading_text).getvalue(),
            f"LOGOS_Findings_{st.session_state.topic}.pdf",
            "application/pdf"
        )