# ==============================
# UI_WELCOME
# ==============================

import streamlit as st
import plotly.graph_objects as go
import numpy as np
from config import PLANES  # Assumes config.py has PLANES = ["Foundation", "Vitality", ...]

def show_welcome():
    st.title("🌟 LOGOS Heptagon Revealer")
    st.markdown("**A 7×7 Metaphysical Diagnostic for Real-Life Questions Powered by AI**")
    
    # Heptagon Gem: Interactive 3D Model
    st.subheader("The Heptagon Gem: 7 Planes of Resonance")
    fig = go.Figure()
    
    # Generate 7 vertices for a heptagon in 3D (simple projection for "gem" effect)
    theta = np.linspace(0, 2*np.pi, 8)[:-1]  # 7 points
    x = np.cos(theta)
    y = np.sin(theta)
    z = np.zeros(7)  # Flat base; elevate for gem sparkle
    z += np.random.uniform(0, 0.5, 7)  # Slight irregularity for "gem" facets
    
    # Add vertices and edges
    fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='markers+lines+text',
                               text=PLANES, textposition="middle center",
                               marker=dict(size=10, color='gold'),
                               line=dict(color='purple', width=3),
                               name="Planes"))
    
    # Hover text for metaphysical tooltips
    hover_text = [f"Plane {i+1}: {plane}<br>Explore stability & growth" for i, plane in enumerate(PLANES)]
    fig.update_traces(hovertemplate='<b>%{text}</b><br>%{hovertext}<extra></extra>')
    
    fig.update_layout(scene=dict(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False),
                      title="Interactive Heptagon Gem", height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    Welcome to the Heptagon – where questions meet cosmic structure.  
    Enter a real-life dilemma, and let the 7×7 matrix reveal hidden resonances.  
    """)
    
    if st.button("🚀 Start Analysis", type="primary"):
        st.session_state.first_run = False
        st.rerun()
    
    # Sample
    st.markdown("**Sample Question:** Should I relocate for a new job?")
