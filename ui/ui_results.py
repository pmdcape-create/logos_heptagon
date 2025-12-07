# ==============================
# UI_RESULTS
# ==============================

# /mount/src/logos_heptagon/ui/ui_results.py

# ==============================
# UI_RESULTS
# ==============================

import streamlit as st
from utils.exports import export_pdf, export_html_grid

def show_results():
    
    # 🚨 CRITICAL GUARD CLAUSE: Must be the very first execution step 🚨
    # Check if the summary text OR the dataframe is missing.
    if st.session_state.summary_text is None or st.session_state.df is None:
        st.error("Data Missing: Cannot display or export results. The previous LLM processing step likely failed to generate the summary or the 7x7 Grid.")
        st.info("Please refresh the app and try confirming your topic again. Check the app logs for details on the LLM failure.")
        return # Exit the function immediately to prevent the TypeError
    
    # --- If the guard passes, the data is safe to use ---

    st.header("📊 Summary Assessment")
    
    # On-Screen Summary
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Resonance Coherence Score", f"{st.session_state.coherence_score}%")
        st.caption("High % = Strong alignment in metaphysical planes.")
    with col2:
        st.metric("Heptagonal Ratio", f"{st.session_state.ratio}:1")
        st.caption("Balance between planes; ideal ~3:1.")
        
    st.markdown("**Key Insights:**")
    st.write(st.session_state.summary_text)
    
    # 7x7 Grid Preview (non-downloadable)
    st.subheader("7×7 Resonance Grid Preview")
    st.dataframe(st.session_state.df, use_container_width=True)
    
    # Downloads (Visible only if API ready)
    if st.session_state.api_ready:
        col_pdf, col_html = st.columns(2)
        with col_pdf:
            # The function call is now safe
            st.download_button("📄 Download Summary Report (PDF)", 
                               data=export_pdf(st.session_state.summary_text, st.session_state.df),
                               file_name="logos_heptagon_summary.pdf",
                               mime="application/pdf")
        with col_html:
            st.download_button("📊 Download 7×7 Grid (HTML)", 
                               data=export_html_grid(st.session_state.df),
                               file_name="logos_heptagon_grid.html",
                               mime="text/html")
    else:
        st.warning("Set API key in sidebar to download.")
        
