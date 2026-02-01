import streamlit as st
from valuation import get_stock_data, value_stock
from content_agent import generate_content

st.title("📊 AI Stock Valuation & Content Generator")

ticker = st.text_input("Enter Stock Ticker (e.g. AAPL)")

if st.button("Analyze Stock"):
    data = get_stock_data(ticker)

    # Check if EPS exists
    if not data["eps"]:
        st.error("EPS data not available for this stock.")
    else:
        valuation = value_stock(data["eps"], data["price"])

        st.subheader(f"{data['name']} ({ticker})")
        st.write("Current Price:", data["price"])
        st.write("EPS:", data["eps"])
        st.metric("Base Value", valuation["Base Value"])
        st.metric("Bull Value", valuation["Bull Value"])
        st.metric("Bear Value", valuation["Bear Value"])
        st.metric("Margin of Safety (%)", valuation["Margin of Safety (%)"])
        st.success(f"Final Verdict: {valuation['Verdict']}")

        # Generate AI content using Hugging Face
        
st.subheader("📢 AI Generated Content")

x_thread = generate_x_thread(data['name'], data['price'], valuation)
st.markdown("**X Thread:**")
st.write(x_thread)

youtube_script = generate_youtube_script(data['name'], data['price'], valuation)
st.markdown("**YouTube Script:**")
st.write(youtube_script)

instagram_caption = generate_instagram_caption(data['name'], data['price'], valuation)
st.markdown("**Instagram Caption:**")
st.write(instagram_caption)
