# logic/analysis.py
import pandas as pd
from utils.api import get_llm_client

# Use the planes & layers from your config.py
from config import planes as PLANES, layers as LAYERS

def run_full_analysis(client, question: str, topics):
    """
    This is the core 7×7 engine.
    For now a fast placeholder that returns realistic-looking data.
    Replace with your original full version whenever you want.
    """
    import random

    data = {}
    for plane in PLANES:
        data[plane] = {}
        for layer in LAYERS:
            # Simulate short insights
            words = ["alignment", "blockage", "flow", "tension", "clarity", "growth", "harmony"]
            data[plane][layer] = random.choice(words).capitalize() + " in this domain"

    df = pd.DataFrame(data, index=LAYERS)
    df.index.name = "Layer → Plane ↓"

    # Fake but realistic scores
    coherence = round(random.uniform(68, 96), 1)
    ratio = round(random.uniform(2.8, 4.2), 2)

    summary = f"""
Your question: {question}
Interpreted as: {' – '.join(topics)}

Resonance Coherence: {coherence}%
Heptagonal Ratio: {ratio}:1

The matrix reveals {'strong' if coherence > 80 else 'moderate'} overall alignment across the seven planes.
Key themes: {' • '.join(topics[:4])}
"""

    return df, summary.strip(), coherence, ratio
