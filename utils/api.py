import streamlit as st
import os
from groq import Groq # Only the Groq client is imported

def setup_api_key():
    
    # 1. INITIALIZE SESSION STATE
    if 'api_key' not in st.session_state:
        st.session_state.api_key = st.secrets.get("GROQ_API_KEY", None)
        
    if 'api_ready' not in st.session_state:
        st.session_state.api_ready = bool(st.session_state.api_key)
        
    # The Groq model to use for the validation check
    validation_model = "llama3-8b-8192" 
    
    with st.expander("Enter Your Groq API Key (Temporary)", expanded=not st.session_state.api_ready):
        # We need a temporary variable for the text input value
        input_value = st.session_state.api_key if st.session_state.api_ready else ""
        
        key = st.text_input(
            "Paste your Groq key here:", 
            type="password", 
            value=input_value
        )
        
        if st.button("Load Key"):
            if key:
                # Test validation
                try:
                    # SIMPLIFIED: Assume key is Groq and try to initialize client
                    client = Groq(api_key=key) 
                    
                    # Simple test prompt
                    client.chat.completions.create(
                        model=validation_model,
                        messages=[{"role": "user", "content": "Test"}]
                    )
                    
                    # On successful validation:
                    st.session_state.api_key = key
                    os.environ["API_KEY"] = key # For utils
                    st.session_state.api_ready = True
                    st.success("Groq Key validated! Rerunning app...")
                    
                    # Force a rerun to update the main flow
                    st.rerun() 
                    
                except Exception as e:
                    # Catch the validation error here (e.g., 401 Unauthorized)
                    st.error(f"Invalid Groq key or validation failed. Error: {e}")
            else:
                st.error("Enter a key.")
    
    # Return the current key from session state
    return st.session_state.get('api_key')

def get_llm_client():
    key = os.environ.get("API_KEY") or st.session_state.get('api_key')
    
    if not key:
        return None # Return None if no key is found
        
    # SIMPLIFIED: Only return the Groq client
    return Groq(api_key=key)
