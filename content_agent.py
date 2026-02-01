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

Write a short social media post summarizing this stock (simple language, risk-focused):
"""

    with st.spinner("Generating AI content... ⏳"):
        results = model(prompt, max_length=150, do_sample=True)
    return results[0]['generated_text']
