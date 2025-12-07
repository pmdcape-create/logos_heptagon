from utils.api import get_llm_client

def extract_key_topics(client, question):
    prompt = f"""
    Extract 3-5 key topics/aspects that underpin this question for metaphysical analysis.
    Focus on core themes (e.g., career, relationships). Output as hyphen-joined phrases only.
    Question: {question}
    Example Output: career-transition-risk-personal-growth
    """
    
    response = client.chat.completions.create(model="llama-3.1-8b-instant",  # Use the current Groq model
                                              messages=[{"role": "user", "content": prompt}])
    topics_str = response.choices[0].message.content.strip()
    return [t.strip() for t in topics_str.split("-") if t.strip()]
