import streamlit as st

# Test import
try:
    from content_agent import generate_content
    st.success("✅ content_agent.py imported successfully!")
except Exception as e:
    st.error(f"❌ Import failed: {e}")
