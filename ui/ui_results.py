# ==============================
# UI_RESULTS
# ==============================

import streamlit as st
import os
import pandas as pd

def show_results():
    st.markdown("<h1 style='text-align: center; margin-top: 50px;'>Your LOGOS Heptagon</h1>", 
                unsafe_allow_html=True)

    topic = st.session_state.get('topic', 'your topic')
    st.markdown(f"<h3 style='text-align: center; color: #666;'>Analysis of: <strong>“{topic}”</strong></h3><br>", 
                unsafe_allow_html=True)

    if 'df' not in st.session_state or st.session_state.df is None:
        st.error("No analysis yet.")
        st.stop()

    df = st.session_state.df
    summary = st.session_state.get('summary', 'No summary available.')

    # Summary always shows
    st.markdown("### Overall Assessment")
    st.write(summary)

    # Demo vs. Full: Use API key presence as proxy (for testing)
    is_paid = 'XAI_API_KEY' in os.environ or 'OPENAI_API_KEY' in os.environ

    if not is_paid:
        st.info("🔓 Demo Mode: Free sample. Unlock full + PDF for R50 via PayFast.")
        # Teaser: First 3 rows + "..."
        teaser_df = df.head(3).copy()
        teaser_df = pd.concat([teaser_df, pd.DataFrame([["...", "...", "..."]], columns=df.columns)], ignore_index=True)
        st.dataframe(teaser_df, use_container_width=True, hide_index=True)
        st.line_chart(teaser_df['strength'].head(3))
        
        if st.button("Unlock Full (Test Mode)"):
            st.session_state.paid = True
            st.rerun()
    else:
        st.success("✅ Full Mode Unlocked! (Powered by Grok xAI)")
        st.caption(f"Generated with {st.session_state.get('api_used', 'API')}")
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.line_chart(df.set_index('name')['strength'])
        
        # Placeholder PDF (we'll make real next)
        st.download_button(
            label="📄 Download Full PDF Report",
            data=f"Full LOGOS Heptagon for '{topic}':\n\n{summary}\n\n{df.to_string()}",  # Simple text for now
            file_name=f"logos_heptagon_{topic.replace(' ', '_')}.txt",  # .txt until real PDF
            mime="text/plain"
        )

    st.markdown("---")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("New Analysis", type="primary", use_container_width=True):
            st.session_state.clear()
            st.rerun()
