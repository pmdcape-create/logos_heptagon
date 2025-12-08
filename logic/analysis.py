# logic/analysis.py
# FULLY RESTORED & PERFECTLY INDENTED LOGOS ENGINE

import pandas as pd
import streamlit as st
import re
from utils.api import get_llm_client
from config import planes as PLANES, layers as LAYERS

# =============================================
# 49 SACRED QUESTIONS (exact sacred order)
# =============================================
NODE_QUESTIONS = [
    # Layer 1 – Purpose
    "From pure potential, what specific impulse is trying to become real through this situation?",
    "What is the original spark of being behind this question?",
    "What unique entity or event is seeking instantiation right now?",
    "What is the divine intention wanting to take form here?",
    "What seed of purpose is buried in this moment?",
    "What is the soul-level reason this is appearing now?",
    "What eternal pattern is choosing this exact vehicle of expression?",

    # Layer 2 – Information/Truth
    "What truth is this situation protecting?",
    "Where is information being sustained or distorted?",
    "What identity or story is being maintained across time?",
    "What feedback loop from higher layers is active?",
    "What belief is currently defining continuity?",
    "What data stream is governing perception?",
    "What hidden knowledge is ready to surface?",

    # Layer 3 – Design
    "How is this situation currently affecting its environment?",
    "What impact pattern is already visible?",
    "What observable outcome is being sculpted?",
    "Where is the design most elegant or most fractured?",
    "What environmental resonance is strongest?",
    "What consequence field is forming?",
    "What footprint will this leave in spacetime?",

    # Layer 4 – Creation (Integration)
    "How are layers 1–3 currently interacting?",
    "What is the arena of experience right now?",
    "Where is spacetime being woven or torn?",
    "What integration is succeeding or failing?",
    "What is the current theatre of evolution?",
    "What container is holding this process?",
    "What alchemical vessel is active?",

    # Layer 5 – Refinement
    "Where is choice or adaptation happening?",
    "What probabilistic collapse is imminent?",
    "What decision point carries the most weight?",
    "Where is refinement pressure strongest?",
    "What timeline branch is crystallising?",
    "What free-will node is illuminated?",
    "What quantum of decision is being offered?",

    # Layer 6 – Revelation (Soul Blueprint)
    "What soul-level principle is governing this?",
    "What law of coherence is being enforced?",
    "What blueprint deviation or alignment exists?",
    "What revelation gate is opening or closing?",
    "What higher-order pattern is now visible?",
    "What soul contract clause is active?",
    "What governance structure is revealing itself?",

    # Layer 7 – Continuity (Divine)
    "What ultimate direction is being offered?",
    "What ultimate direction is being offered?",
    "Where is divine consciousness itself steering?",
    "What divine alignment is possible here?",
    "What eternal continuity is seeking expression?",
    "What final-purpose vector is dominant?",
    "Where is the hand of Grace most evident?",
   
