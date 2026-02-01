import math

def stock_valuation(
    price,
    eps_ttm,
    eps_fwd,
    roe,
    debt_equity,
    wacc=0.10,
    terminal_growth=0.03
):
    # Growth assumptions
    base_growth = 0.08
    bull_growth = 0.12
    bear_growth = 0.04

    # Scenario selection
    scenario = "Base"
    selected_growth = base_growth

    # ---- DCF 5Y ----
    dcf_5y = 0
    eps = eps_ttm

    for year in range(1, 6):
        eps *= (1 + selected_growth)
        dcf_5y += eps / ((1 + wacc) ** year)

    terminal_value = (eps * (1 + terminal_growth)) / (wacc - terminal_growth)
    terminal_discounted = terminal_value / ((1 + wacc) ** 5)

    dcf_5y += terminal_discounted

    # ---- DCF 10Y ----
    dcf_10y = 0
    eps = eps_ttm

    for year in range(1, 11):
        eps *= (1 + selected_growth)
        dcf_10y += eps / ((1 + wacc) ** year)

    terminal_value_10 = (eps * (1 + terminal_growth)) / (wacc - terminal_growth)
    terminal_discounted_10 = terminal_value_10 / ((1 + wacc) ** 10)

    dcf_10y += terminal_discounted_10

    # ---- Graham Formula ----
    graham_value = eps_ttm * (8.5 + 2 * (base_growth * 100))

    # ---- Final Intrinsic Value ----
    final_intrinsic = round((dcf_5y + dcf_10y + graham_value) / 3, 2)

    # ---- Margin of Safety ----
    margin_of_safety = round(((final_intrinsic - price) / price) * 100, 2)

    # ---- Signal ----
    if margin_of_safety > 25:
        signal = "BUY"
    elif margin_of_safety > 0:
        signal = "HOLD"
    else:
        signal = "SELL"

    # ---- Risk Flag ----
    risk_flag = "LOW"
    if debt_equity > 1 or roe < 10:
        risk_flag = "HIGH"

    return {
        "Price": price,
        "EPS_TTM": eps_ttm,
        "EPS_Fwd": eps_fwd,
        "Base_Growth_%": base_growth * 100,
        "Bull_Growth_%": bull_growth * 100,
        "Bear_Growth_%": bear_growth * 100,
        "Scenario": scenario,
        "Selected_Growth_%": selected_growth * 100,
        "WACC_%": wacc * 100,
        "Terminal_Growth_%": terminal_growth * 100,
        "ROE_%": roe,
        "Debt_Equity": debt_equity,
        "DCF_5Y": round(dcf_5y, 2),
        "DCF_10Y": round(dcf_10y, 2),
        "Graham_Value": round(graham_value, 2),
        "Final_Intrinsic": final_intrinsic,
        "Margin_of_Safety_%": margin_of_safety,
        "Signal": signal,
        "Risk_Flag": risk_flag
    }
