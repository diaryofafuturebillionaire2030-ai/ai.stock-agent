import yfinance as yf

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        "price": info.get("currentPrice"),
        "eps": info.get("trailingEps"),
        "name": info.get("shortName")
    }

def value_stock(eps, price):
    base_pe = 15
    bull_pe = 20
    bear_pe = 10

    base = eps * base_pe
    bull = eps * bull_pe
    bear = eps * bear_pe

    margin_safety = ((base - price) / base) * 100

    verdict = (
        "Undervalued" if price < bear else
        "Fairly Valued" if price <= base else
        "Overvalued"
    )

    return {
        "Base Value": round(base, 2),
        "Bull Value": round(bull, 2),
        "Bear Value": round(bear, 2),
        "Margin of Safety (%)": round(margin_safety, 2),
        "Verdict": verdict
    }
