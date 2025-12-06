# ==============================
# LOGIC_ANALYSIS (skeleton)
# ==============================

import time
import streamlit as st
from config import matrix_questions

def analyse(topic: str, llm):
    matrix = []
    with st.spinner("Running LOGOS 7×7 analysis…"):
        for row in matrix_questions:
            row_cells = []
            for q in row:
                prompt = f"""
                You are a wise and friendly expert blending physics and metaphysics.
                Topic: {topic}
                Grid Question: {q}

                Provide an answer for this exact node.
                Blend universal truth, current physics concepts (entanglement, resonance, fields, non-locality), and the metaphysical LOGOS model.
                Keep it concise (8–15 words), profound, and focused on interconnectedness.
                If the topic involves speculative phenomena, acknowledge possible metaphysical interpretations while neutrally noting lack of direct empirical evidence.
                """

                max_retries = 3
                ans = "…"
                for attempt in range(max_retries):
                    try:
                        ans = llm.invoke(prompt).content.strip()
                        break
                    except Exception as e:
                        if "429" in str(e):
                            wait = 60 if attempt == 0 else 120
                            st.warning(f"Rate limit — pausing {wait}s (attempt {attempt + 1})")
                            time.sleep(wait)
                        else:
                            st.error(f"Error: {e}")
                            break
                row_cells.append(ans)
            matrix.append(row_cells)
    return matrix