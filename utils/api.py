import streamlit as st
import os
from groq import Groq # Assumes installed
from openai import OpenAI # Need to import OpenAI client

def setup_api_key():
    
    # In utils/api.py (Corrected Initial State Setup)

if 'api_key' not in st.session_state:
    # 1. Load the key from secrets only if it hasn't been loaded yet.
    st.session_state.api_key = st.secrets.get("GROQ_API_KEY", None)
    
if 'api_ready' not in st.session_state:
    # 2. Initialize api_ready based on whether a key was successfully loaded from secrets.
    st.session_state.api_ready = bool(st.session_state.api_key)
        
    
    with st.expander("Enter Your API Key (Temporary)"):
        key = st.text_input("Paste Groq/OpenAI Key:", type="password", value=st.session_state.api_key or "")
        if st.button("Load Key"):
            if key:
                # Test validation
                try:
                    client = Groq(api_key=key) if "groq" in key.lower() else OpenAI(api_key=key)
                    # Simple test prompt
                    response = client.chat.completions.create(model="llama3-8b-8192" if "groq" in key.lower() else "gpt-3.5-turbo",
                                                             messages=[{"role": "user", "content": "Test"}])
                    st.session_state.api_key = key
                    os.environ["API_KEY"] = key  # For utils
                    st.session_state.api_ready = True
                    st.success("Key validated!")
                    st.rerun()
                    return key
                except Exception as e:
                    st.error(f"Invalid key: {e}")
            else:
                st.error("Enter a key.")
    return st.session_state.get('api_key')

def get_llm_client():
    key = os.environ.get("API_KEY")
    # Implement Groq/OpenAI client selection here
    return Groq(api_key=key)  # Default to Groq
