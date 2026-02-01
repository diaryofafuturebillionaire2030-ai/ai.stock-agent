import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

model = load_model()

def generate_content(stock, price, valuation):
    prompt = f"""
You are a professional equity research analyst.

Stock: {stock}
Current Price: {price}
Valuation:
Base: {valuation['Base Value']}
Bull: {valuation['Bull Value']}
Bear: {valuation['Bear Value']}
Verdict: {valuation['Verdict']}

Generate:
1. X thread (5 short tweets)
2. YouTube script (1–2 minutes)
3. Instagram caption (short and engaging)

Use simple language, highlight risks, and avoid financial advice.
"""

    with st.spinner("Generating AI content... ⏳"):
        results = model(prompt, max_length=300, do_sample=True)
    return results[0]['generated_text']
