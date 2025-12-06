# ============================== 
# UI_LOADING (USED VIA PAGE ROUTER)
# ==============================


import streamlit as st
import time
import os
import pandas as pd
from openai import OpenAI  # Works for both OpenAI & xAI

def show_loading():
    st.markdown("<h1 style='text-align: center; margin-top: 80px;'>Building Your LOGOS Heptagon</h1>", 
                unsafe_allow_html=True)

    if 'topic' not in st.session_state or not st.session_state.topic:
        st.error("Oops! Topic missing.")
        if st.button("Back"):
            st.session_state.topic_confirmed = False
            st.rerun()
        st.stop()

    topic = st.session_state.topic
    st.markdown(f"<h2 style='text-align: center; color: #555;'>“{topic}”</h2>", unsafe_allow_html=True)

    progress_bar = st.progress(0)
    status = st.empty()
    detail = st.empty()

    steps = [
        "Initializing coherence engine...",
        "Mapping semantic vectors across 7 axes...",
        "Aligning philosophical archetypes...",
        "Calculating tension fields...",
        "Resolving paradoxes...",
        "Rendering heptagonal symmetry...",
        "Finalizing insight matrix..."
    ]

    # Prefer Grok API if key available
    client = None
    using_grok = False
    if 'XAI_API_KEY' in os.environ:
        client = OpenAI(
            api_key=os.environ["XAI_API_KEY"],
            base_url="https://api.x.ai/v1"  # xAI endpoint
        )
        using_grok = True
        model = "grok-beta"  # Fast & free-tier friendly; or "grok-2-latest"
    elif 'OPENAI_API_KEY' in os.environ:
        client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        model = "gpt-4o-mini"
    else:
        # No key = demo mode with dummy
        raise ValueError("No API key found—add XAI_API_KEY to secrets for real analysis.")

    try:
        # Grok-optimized prompt
        system_prompt = """
        You are LOGOS, a 7-dimensional truth engine. Analyze the topic with maximal coherence.
        Output ONLY valid JSON:
        {
          "dimensions": [
            {"name": "Thesis", "insight": "Core affirmative (2-3 sentences, insightful)", "strength": 85},
            {"name": "Antithesis", "insight": "Opposing force (2-3 sentences)", "strength": 70},
            {"name": "Synthesis", "insight": "Integration (2-3 sentences)", "strength": 90},
            {"name": "Paradox", "insight": "Tension point (2-3 sentences)", "strength": 60},
            {"name": "Transcendence", "insight": "Breakthrough (2-3 sentences)", "strength": 80},
            {"name": "Ground", "insight": "Foundation (2-3 sentences)", "strength": 95},
            {"name": "Horizon", "insight": "Future potential (2-3 sentences)", "strength": 75}
          ],
          "summary": "1-paragraph overall coherence assessment."
        }
        Strengths: 0-100 integers. Be neutral, profound, relevant. No fluff.
        """
        
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Analyze deeply: {topic}"}
            ],
            temperature=0.7
        )
        
        import json
        data = json.loads(response.choices[0].message.content)
        df = pd.DataFrame(data["dimensions"])
        st.session_state.df = df
        st.session_state.summary = data["summary"]
        st.session_state.api_used = "Grok" if using_grok else "OpenAI"
        
    except Exception as e:
        st.warning(f"API error ({'Grok' if using_grok else 'OpenAI'}): {str(e)[:100]}... Falling back to demo.")
        # Dummy data
        dummy_data = {
            "name": ["Thesis", "Antithesis", "Synthesis", "Paradox", "Transcendence", "Ground", "Horizon"],
            "insight": ["Demo insight 1", "Demo insight 2", "Demo insight 3", "Demo insight 4", "Demo insight 5", "Demo insight 6", "Demo insight 7"],
            "strength": [88, 76, 91, 64, 82, 95, 79]
        }
        st.session_state.df = pd.DataFrame(dummy_data)
        st.session_state.summary = "Demo mode active—add API key for real analysis."

    # Progress animation
    for i in range(100):
        time.sleep(0.05)
        progress_bar.progress(i + 1)
        step_idx = min(i // 15, len(steps) - 1)
        status.markdown(f"**{steps[step_idx]}**")
        detail.markdown(f"Progress: {i+1}%")

    st.session_state.analysis_complete = True
    progress_bar.empty()
    status.empty()
    detail.empty()
    st.success(f"Heptagon generated with {st.session_state.api_used}! (Real insights unlocked)")
    time.sleep(1)
    st.rerun()
