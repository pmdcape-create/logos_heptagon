# ==============================
# UI_RESULTS
# ==============================

import streamlit as st
from logic.exporters import grid_to_html, reading_to_pdf   # these two functions already exist and work

def show_results():
    # This function is only called when analysis is truly finished
    if st.session_state.get("df") is None or not st.session_state.get("topic_confirmed", False):
        return

    st.success("LOGOS analysis complete")

    st.markdown(f"**Your question:** {st.session_state.natural_sentence}")
    st.markdown(
        f"**Coherence:** {st.session_state.coherence:.1f}%  │  "
        f"**Ratio:** {st.session_state.ratio:.3f}/1.000"
    )

    st.subheader("LOGOS FINDINGS & INTERPRETATION")
    # This is your missing summary assessment — now back!
    st.markdown(st.session_state.reading_text)

    st.markdown("---")
    st.subheader("7×7 Heptagon Data Grid")

    # Beautiful wrapped grid
    styled_df = st.session_state.df.style.set_properties(
        **{
            'text-align': 'left',
            'white-space': 'pre-wrap',
            'font-size': '14px',
            'padding': '10px'
        }
    )
    st.dataframe(styled_df, use_container_width=True)

    # ─────────────────────────────────────
    # Download buttons (exactly like before)
    # ─────────────────────────────────────
    col1, col2 = st.columns(2)

    with col1:
        html_bytes = grid_to_html(
            st.session_state.df,
            st.session_state.topic,
            st.session_state.coherence,
            st.session_state.ratio
        ).getvalue()

        st.download_button(
            label="Download 7×7 Grid (HTML File)",
            data=html_bytes,
            file_name=f"LOGOS_Grid_{st.session_state.topic.replace(' ', '_')}.html",
            mime="text/html"
        )

    with col2:
        pdf_bytes = reading_to_pdf(st.session_state.reading_text).getvalue()

        st.download_button(
            label="Download Findings (Landscape PDF)",
            data=pdf_bytes,
            file_name=f"LOGOS_Findings_{st.session_state.topic.replace(' ', '_')}.pdf",
            mime="application/pdf"
        )
        
