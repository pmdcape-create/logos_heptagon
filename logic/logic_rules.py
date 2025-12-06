# ==============================
# LOGIC_RULES (SIMPLE LOADER)
# ==============================

import json
from pathlib import Path

RULES_PATH = Path(__file__).parent.parent / 'data' / 'rules.json'


def load_rules():
    with open(RULES_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_weight(layer_name):
    rules = load_rules()
    return rules.get('weights', {}).get(layer_name, 1.0)
