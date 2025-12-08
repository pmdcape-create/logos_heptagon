# logic/summary_generator.py
import streamlit as st

SUMMARY_SYSTEM_PROMPT = """
You are an expert metaphysicist and senior consultant for the LOGOS Heptagon system.
You speak in a warm, friendly, slightly formal tone — exactly like a very wise, trustworthy friend who also happens to be a professor of consciousness studies.

Your task is to write a beautiful, readable summary of a completed 7×7 LOGOS analysis.

Structure (always follow this exact order):
1. Opening paragraph (2–4 sentences)
   - Echo the user’s original question or key theme
   - Give a very brief, human overview of what the grid is showing overall
   - Keep it hopeful and empowering

2. Blank line

3. Section “Key Resonances in the Heptagon”
   - List only the 5–8 most significant or unusual cells (the ones with the strongest language, highest entropy shift, or clearest pattern)
   - For each one write 1–2 crystal-clear sentences in plain but precise language
   - Always mention the Layer number + Plane name (e.g. “Layer 5 – Refinement” or “Layer 7 – Continuity”)

4. Closing 2–3 sentences
   - Tie everything back to the user’s life situation
   - End on an encouraging, practical note

Never use bullet points, never number the findings, never sound like a tarot reading.
Use beautiful but understandable language. Keep total length 300–450 words.
"""

def generate_summary(df, user_question: str) -> str:
    # Find the most "alive" cells — simple but very effective heuristic you always loved
    text_cells = df.astype(str).applymap(lambda x: x.lower())
    keywords = ["breakthrough", "collapse", "resonance", "entropy", "alignment", "karmic", "oscillation", 
                "refinement", "revelation", "continuity", "divine", "quantum", "instantiation", "soul"]

    scores = text_cells.applymap(lambda x: sum(word in x for word in keywords))
    top_cells = scores.unstack().sort_values(ascending=False).head(12)

    highlights = []
    for (row, col), _ in top_cells.items():
        layer = row + 1
        plane = df.columns[col]
        cell_text = df.iat[row, col]
        if len(cell_text) > 20:  # ignore tiny cells
            highlights.append(f"{layer} – {plane}: {cell_text.strip()}")

    context = f"""
User question: {user_question}

The 7 most significant observations from the grid (in order of importance):
{"\n".join(highlights[:8])}
"""

    messages = [
        {"role": "system", "content": SUMMARY_SYSTEM_PROMPT},
        {"role": "user", "content": context}
    ]

    try:
        response = st.session_state.llm_client.chat.completions.create(
            model="grok-beta",   # or whatever model you use now
            messages=messages,
            temperature=0.7,
            max_tokens=1200
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"(Summary temporarily unavailable — {str(e)})"
