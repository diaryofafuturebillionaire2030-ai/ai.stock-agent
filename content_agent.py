import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

model = load_model()

def generate_x_thread(stock, price, valuation):
    prompt = f"""
You are a professional equity research analyst.
Stock: {stock}
Current Price: {price}
Valuation:
Base: {valuation['Base Value']}
Bull: {valuation['Bull Value']}
Bear: {valuation['Bear Value']}
Verdict: {valuation['Verdict']}

Write 5 short tweets (X thread) summarizing this stock. Simple, engaging, and risk-aware.
"""
    with st.spinner("Generating X thread... ⏳"):
        results = model(prompt, max_length=150, do_sample=True)
    return results[0]['generated_text']

def generate_youtube_script(stock, price, valuation):
    prompt = f"""
You are a professional equity research analyst.
Stock: {stock}
Current Price: {price}
Valuation:
Base: {valuation['Base Value']}
Bull: {valuation['Bull Value']}
Bear: {valuation['Bear Value']}
Verdict: {valuation['Verdict']}

Write a 1–2 minute YouTube script explaining this stock. Simple language, engaging.
"""
    with st.spinner("Generating YouTube script... ⏳"):
        results = model(prompt, max_length=200, do_sample=True)
    return results[0]['generated_text']

def generate_instagram_caption(stock, price, valuation):
    prompt = f"""
You are a professional equity research analyst.
Stock: {stock}
Current Price: {price}
Valuation:
Base: {valuation['Base Value']}
Bull: {valuation['Bull Value']}
Bear: {valuation['Bear Value']}
Verdict: {valuation['Verdict']}

Write a short, catchy Instagram caption about this stock.
"""
    with st.spinner("Generating Instagram caption... ⏳"):
        results = model(prompt, max_length=100, do_sample=True)
    return results[0]['generated_text']
