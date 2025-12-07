import streamlit as st
import os
from groq import Groq # Assumes installed
from openai import OpenAI # Need to import OpenAI client

def setup_api_key():
    
    # 1. INITIALIZE SESSION STATE (MOVED INSIDE THE FUNCTION)
    # This logic must be indented under the function definition.
    if 'api_key' not in st.session_state:
        # Load the key from secrets only if it hasn't been loaded yet.
        st.session_state.api_key = st.secrets.get("GROQ_API_KEY", None)
        
    if 'api_ready' not in st.session_state:
        # Initialize api_ready based on whether a key was successfully loaded from secrets.
        st.session_state.api_ready = bool(st.session_state.api_key)
        
    # If the key is already loaded and ready, we don't need to show the expander on every run.
    # However, since you want to allow changing it, we continue to display the input/button.
    
    with st.expander("Enter Your API Key (Temporary)", expanded=not st.session_state.api_ready):
        # We need a temporary variable for the text input value to avoid errors during validation
        input_value = st.session_state.api_key if st.session_state.api_ready else ""
        
        key = st.text_input(
            "Paste Groq/OpenAI Key:", 
            type="password", 
            # Use the input_value from the session state or blank if not ready
            value=input_value
        )
        
        if st.button("Load Key"):
            if key:
                # Test validation
                try:
                    # Determine client based on key format (approximate)
                    # In utils/api.py, inside the try block:

                # ...
                try:
                    # Check if the key starts with the Groq prefix 'pk-'
                    is_groq = key.lower().startswith("pk-") 
    
                    # Use Groq client if it's a Groq key, otherwise use OpenAI
                    client = Groq(api_key=key) if is_groq else OpenAI(api_key=key)
                    # ...
                    
                    # Simple test prompt
                    model = "llama3-8b-8192" if is_groq else "gpt-3.5-turbo"
                    client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": "Test"}]
                    )
                    
                    # On successful validation:
                    st.session_state.api_key = key
                    os.environ["API_KEY"] = key # For utils
                    st.session_state.api_ready = True
                    st.success("Key validated! Rerunning app...")
                    
                    # Force a rerun to update the main flow
                    st.rerun() 
                    
                except Exception as e:
                    st.error(f"Invalid key or validation failed. Error: {e}")
            else:
                st.error("Enter a key.")
    
    # Return the current key from session state
    return st.session_state.get('api_key')

def get_llm_client():
    key = os.environ.get("API_KEY") or st.session_state.get('api_key')
    
    if not key:
        return None # Return None if no key is found
        
    # Determine client based on key format
    is_groq = "groq" in key.lower() and not "openai" in key.lower()
    
    return Groq(api_key=key) if is_groq else OpenAI(api_key=key)
