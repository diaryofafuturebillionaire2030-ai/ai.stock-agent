import streamlit as st
import yfinance as yf

from content_agent import (
    generate_x_thread,
    generate_youtube_script,
    generate_instagram_caption
)

from valuation import stock_valuation

# ------------------ PAGE SETUP ------------------
st.set_page_config(
    page_title="AI Stock Valuation Agent",
    layout="centered"
)

st.title("📊 AI Stock Valuation Agent")

# ------------------ USER INPUT ------------------
ticker = st.text_input("Enter Stock Ticker (e.g. NVDA, AAPL, MSFT)")

if ticker:
    stock = yf.Ticker(ticker)
    info = stock.info

    price = info.get("currentPrice")
    eps_ttm = info.get("trailingEps")
    eps_fwd = info.get("forwardEps", eps_ttm)
    roe = info.get("returnOnEquity", 0)
    debt_equity = info.get("debtToEquity", 0)

    # Convert ROE to %
    roe = roe * 100 if roe else 0

    if price is None or eps_ttm is None:
        st.error("❌ Unable to fetch complete stock data. Try another ticker.")
    else:
        # ------------------ BASIC INFO ------------------
        st.subheader("📈 Stock Information")
        st.write(f"**Price:** ${price}")
        st.write(f"**EPS (TTM):** {eps_ttm}")
        st.write(f"**EPS (Forward):** {eps_fwd}")
        st.write(f"**ROE (%):** {round(roe,2)}")
        st.write(f"**Debt / Equity:** {debt_equity}")

        # ------------------ VALUATION ENGINE ------------------
        valuation = stock_valuation(
            price=price,
            eps_ttm=eps_ttm,
            eps_fwd=eps_fwd,
            roe=roe,
            debt_equity=debt_equity
        )

        st.subheader("💰 Full Valuation Output")

        for key, value in valuation.items():
            st.write(f"**{key}:** {value}")

        # ------------------ AI CONTENT ------------------
        st.subheader("🧠 AI Generated Content")

        if st.button("Generate X (Twitter) Thread"):
            with st.spinner("Generating X thread..."):
                st.write(
                    generate_x_thread(
                        ticker,
                        price,
                        valuation["Final_Intrinsic"],
                        valuation["Bull_Growth_%"],
                        valuation["Bear_Growth_%"]
                    )
                )

        if st.button("Generate YouTube Script"):
            with st.spinner("Generating YouTube script..."):
                st.write(
                    generate_youtube_script(
                        ticker,
                        price,
                        valuation["Final_Intrinsic"],
                        valuation["Bull_Growth_%"],
                        valuation["Bear_Growth_%"]
                    )
                )

        if st.button("Generate Instagram Caption"):
            with st.spinner("Generating Instagram caption..."):
                st.write(
                    generate_instagram_caption(
                        ticker,
                        price,
                        valuation["Final_Intrinsic"],
                        valuation["Bull_Growth_%"],
                        valuation["Bear_Growth_%"]
                    )
                )
