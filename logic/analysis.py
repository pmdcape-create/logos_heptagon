# logic/analysis.py
import pandas as pd
import streamlit as st
import re
from utils.api import get_llm_client
from config import planes as PLANES, layers as LAYERS

NODE_QUESTIONS = [
    "From pure potential, what specific impulse is trying to become real through this situation?",
    "What is the original spark of being behind this question?",
    "What unique entity or event is seeking instantiation right now?",
    "What is the divine intention wanting to take form here?",
    "What seed of purpose is buried in this moment?",
    "What is the soul-level reason this is appearing now?",
    "What eternal pattern is choosing this exact vehicle of expression?",

    "What truth is this situation protecting?",
    "Where is information being sustained or distorted?",
    "What identity or story is being maintained across time?",
    "What feedback loop from higher layers is active?",
    "What belief is currently defining continuity?",
    "What data stream is governing perception?",
    "What hidden knowledge is ready to surface?",

    "How is this situation currently affecting its environment?",
    "What impact pattern is already visible?",
    "What observable outcome is being sculpted?",
    "Where is the design most elegant or most fractured?",
    "What environmental resonance is strongest?",
    "What consequence field is forming?",
    "What footprint will this leave in spacetime?",

    "How are layers 1–3 currently interacting?",
    "What is the arena of experience right now?",
    "Where is spacetime being woven or torn?",
    "What integration is succeeding or failing?",
    "What is the current theatre of evolution?",
    "What container is holding this process?",
    "What alchemical vessel is active?",

    "Where is choice or adaptation happening?",
    "What probabilistic collapse is imminent?",
    "What decision point carries the most weight?",
    "Where is refinement pressure strongest?",
    "What timeline branch is crystallising?",
    "What free-will node is illuminated?",
    "What quantum of decision is being offered?",

    "What soul-level principle is governing this?",
    "What law of coherence is being enforced?",
    "What blueprint deviation or alignment exists?",
    "What revelation gate is opening or closing?",
    "What higher-order pattern is now visible?",
    "What soul contract clause is active?",
    "What governance structure is revealing itself?",

    "What ultimate direction is being offered?",
    "Where is divine consciousness itself steering?",
    "What divine alignment is possible here?",
    "What eternal continuity is seeking expression?",
    "What final-purpose vector is dominant?",
    "Where is the hand of Grace most evident?",
    "What will remain when everything else falls away?"
]

SYSTEM_PROMPT = """
You are the LOGOS Heptagon intelligence — a warm, wise, slightly formal metaphysical expert.
Answer ONLY with the direct insight for this exact cell.
One to three short, powerful sentences. Never use bullet points or numbering.
Use precise terms when correct, but always make it beautiful and understandable.
Tone: friendly, encouraging, profound — like a trusted mentor.
"""

@st.cache_data(show_spinner=False)
def run_full_analysis(_client, question: str, topics) -> tuple:
    df = pd.DataFrame(index=LAYERS, columns=PLANES)
    
    progress = st.progress(0)
    status = st.empty()
    status.write("Running sacred LOGOS 7×7 analysis…")

    for idx, node_question in enumerate(NODE_QUESTIONS):
        layer_idx = idx // 7
        plane_idx = idx % 7
        
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"User's real-life question: {question}\n\nSpecific node question: {node_question}"}
        ]

        try:
            response = _client.chat.completions.create(
                model="grok-beta",
                messages=messages,
                temperature=0.7,
                max_tokens=180
            )
            answer = response.choices[0].message.content.strip()
        except Exception:
            answer = "(momentary pause in revelation)"

        df.iat[layer_idx, plane_idx] = answer
        progress.progress((idx + 1) / 49)

    status.empty()
    progress.empty()

    # Coherence
    all_text = " ".join(df.astype(str).values.flatten()).lower()
    positive = len(re.findall(r'\b(alignment|flow|clarity|growth|harmony|resonance|grace|continuity|revelation)\b', all_text))
    negative = len(re.findall(r'\b(blockage|tension|distortion|collapse|entropy|karmic|fracture)\b', all_text))
    coherence = round(50 + (positive - negative) * 3.2, 1)
    coherence = max(42, min(98, coherence))
    ratio = round(coherence / 22.5, 3)

    # Summary
    try:
        from logic.summary_generator import generate_summary
        summary = generate_summary(df, question)
    except Exception:
        summary = "The full interpretation is being prepared."

    return df, summary, coherence, ratio   
