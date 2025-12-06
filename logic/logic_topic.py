import re

def sentence_to_topic(sentence: str) -> str:
    if not sentence.strip():
        return "Unknown"
    
    # Extract numbers
    numbers = re.findall(r'\b\d+%|\b\d+\b', sentence)
    numbers_clean = [
        n.replace('%', 'Percent') if '%' in n else f"Age{n}" if len(n) > 2 and int(n) >= 30 else n
        for n in numbers
    ]
    
    # Clean words
    stop_words = {'i','me','my','we','you','he','she','it','they','the','a','an','and','but','if','or',
                  'what','when','how','will','should','can','just','now','please','do'}
    words = re.findall(r'\b[a-zA-Z]{3,}\b', sentence.lower())
    clean_words = [w.capitalize() for w in words if w not in stop_words]
    
    # Combine & dedupe preserving order
    parts = numbers_clean + clean_words
    seen = set()
    unique = [p for p in parts if not (p in seen or seen.add(p))]
    
    return "–".join(unique) if unique else "Unknown"