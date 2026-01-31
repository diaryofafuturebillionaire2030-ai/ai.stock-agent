import openai
import streamlit as st

# This will read your API key from GitHub / Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_content(stock, price, valuation):
    prompt = f"""
You are a professional equity research analyst and finance content creator.

Stock: {stock}
Current Price: {price}
Valuation:
Base: {valuation['Base Value']}
Bull: {valuation['Bull Value']}
Bear: {valuation['Bear Value']}
Verdict: {valuation['Verdict']}

Create:
1. A viral X thread (5 tweets)
2. A YouTube script (1–2 minutes)
3. A short Instagram caption

Rules:
- Simple language
- Risk-focused
- No financial advice
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6
    )

    return response.choices[0].message.content
