import streamlit as st
import yfinance as yf

st.title("Stock Data Test ✅")

ticker = st.text_input("Enter Stock Ticker (e.g. AAPL)")

if st.button("Get Stock Info"):
    stock = yf.Ticker(ticker)
    info = stock.info
    st.write("Stock Name:", info.get("shortName"))
    st.write("Current Price:", info.get("currentPrice"))
    st.write("EPS:", info.get("trailingEps"))
