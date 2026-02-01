import streamlit as st
import yfinance as yf

from content_agent import (
    generate_x_thread,
    generate_youtube_script,
    generate_instagram_caption
)

st.title("📊 AI Stock Valuation Agent")

ticker = st.text_input("Enter Stock Ticker (e.g. NVDA, AAPL)")

if ticker:
    stock = yf.Ticker(ticker)
    price = stock.info.get("currentPrice", "N/A")
    eps = stock.info.get("trailingEps", "N/A")

    st.subheader("📈 Stock Info")
    st.write(f"**Current Price:** {price}")
    st.write(f"**EPS:** {eps}")

    # Simple valuation logic
    base_value = round(eps * 15, 2) if eps != "N/A" else "N/A"
    bull_value = round(eps * 20, 2) if eps != "N/A" else "N/A"
    bear_value = round(eps * 10, 2) if eps != "N/A" else "N/A"

    st.subheader("💰 Valuation")
    st.write(f"Base Value: {base_value}")
    st.write(f"Bull Value: {bull_value}")
    st.write(f"Bear Value: {bear_value}")

    st.subheader("🧠 AI Content")

    if st.button("Generate X Thread"):
        st.write(generate_x_thread(ticker, price, base_value, bull_value, bear_value))

    if st.button("Generate YouTube Script"):
        st.write(generate_youtube_script(ticker, price, base_value, bull_value, bear_value))

    if st.button("Generate Instagram Caption"):
        st.write(generate_instagram_caption(ticker, price, base_value, bull_value, bear_value))
