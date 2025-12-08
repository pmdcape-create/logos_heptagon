   # ==============================
# ui/ui_results.py
# ==============================

import streamlit as st
from logic.exporters import grid_to_html, reading_to_pdf


def show_results():
    # Safety guard — only show results when analysis is truly complete
    if st.session_state.get("df") is None or not st.session_state.get("topic_confirmed", False):
        return

    st.success("LOGOS analysis complete")

    # ─────────────────────────────────────
    # Safe access to all session state values (no more KeyError/AttributeError)
    # ─────────────────────────────────────
    question = (
        st.session_state.get("natural_sentence") or
        st.session_state.get("topic", "Your question")
    )

    coherence = st.session_state.get("coherence", 0.0)
    ratio = st.session_state.get("ratio", 0.0)
    reading_text = st.session_state.get("reading_text", "Analysis complete — findings displayed in the grid below.")
    topic = st.session_state.get("topic", "LOGOS_Analysis")

    # ─────────────────────────────────────
    # Display results
    # ─────────────────────────────────────
    st.markdown(f"**Your question:** {question}")
    st.markdown(f"**Coherence:** {coherence:.1f}%  │  **Ratio:** {ratio:.3f}/1.000")

    st.subheader("LOGOS FINDINGS & INTERPRETATION")
    st.markdown(reading_text)

    st.markdown("---")
    st.subheader("7×7 Heptagon Data Grid")

    # Beautiful, readable grid
    styled_df = st.session_state.df.style.set_properties(**{
        'text-align': 'left',
        'white-space': 'pre-wrap',
        'font-size': '14px',
        'padding': '10px',
        'background-color': '#fafafa'
    })
    st.dataframe(styled_df, use_container_width=True)

    # ─────────────────────────────────────
    # Download buttons — safe fallbacks
    # ──────────────────────────────────────
    col1, col2 = st.columns(2)

    with col1:
        try:
            html_data = grid_to_html(
                st.session_state.df,
                topic,
                coherence,
                ratio
            ).getvalue()
            st.download_button(
                label="Download 7×7 Grid (HTML File)",
                data=html_data,
                file_name=f"LOGOS_Grid_{topic.replace(' ', '_')}.html",
                mime="text/html"
            )
        except Exception:
            st.error("HTML export temporarily unavailable")

    with col2:
        try:
            pdf_data = reading_to_pdf(reading_text).getvalue()
            st.download_button(
                label="Download Findings (Landscape PDF)",
                data=pdf_data,
                file_name=f"LOGOS_Findings_{topic.replace(' ', '_')}.pdf",
                mime="application/pdf"
            )
        except Exception:
            st.error("PDF export temporarily unavailable")
