def generate_structured_reading(topic, natural_sentence, coherence, ratio, grid_df, llm):
    try:
        cells = [
            grid_df.loc["Decision Quantum", "Revelation"],
            grid_df.loc["Blueprint / Soul", "Refinement"],
            grid_df.loc["Creator Layer", "Revelation"],
            grid_df.loc["Existence", "Continuity"],
            grid_df.loc["Instantiation", "Ideation"]
        ]
    except:
        cells = ["…"] * 5

    prompt = f"""
    You are a wise and friendly expert consultant providing deep analysis.
    Goal: clear, honest, warm interpretation blending universal truths, current physics (entanglement, resonance, fields), and the LOGOS metaphysical model.

    User's Question: "{natural_sentence}"
    Interpreted Topic: {topic}
    Coherence of Reading: {coherence:.1f}%
    Strong Interconnection Signals: {" • ".join(cells)}

    Answer structure:
    1. Short, empathetic opening acknowledging the question.
    2. Section titled "**Conceptual Context**" — 1–2 factual paragraphs from philosophy/science (e.g., quantum entanglement, free will debates) explaining the core challenge/implication. Do NOT define the term.
    3. 3–5 numbered, grounded, actionable insights from the LOGOS 7×7 grid.
    4. Clear "Bottom line" paragraph summarizing the revealed truth.
    """

    return llm.invoke(prompt).content.strip()