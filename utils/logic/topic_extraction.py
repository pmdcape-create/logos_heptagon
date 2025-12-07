from utils.api import get_llm_client

def extract_key_topics(client, question):
    prompt = f"""
    Extract 3-5 key topics/aspects that underpin this question for metaphysical analysis.
    Focus on core themes (e.g., career, relationships). Output as hyphen-joined phrases only.
    Question: {question}
    Example Output: career-transition-risk-personal-growth
    """
    response = client.chat.completions.create(model="llama3-8b-8192",  # Or gpt-3.5-turbo
                                              messages=[{"role": "user", "content": prompt}])
    topics_str = response.choices[0].message.content.strip()
    return [t.strip() for t in topics_str.split("-") if t.strip()]
