# app.py
import streamlit as st
import pandas as pd
from scoring import calculate_score # type: ignore
from storage import get_next_trade_id, save_trade
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# --- Google Sheets setup ---
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

creds_dict = st.secrets["google_credentials"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(dict(creds_dict), scope)
client = gspread.authorize(creds)
sheet = client.open_by_key("1_ONSYjb4pjVRMAjCIXAEAkvrU4qHGFkY_nbIIf3MnKw").sheet1

st.set_page_config(page_title="Trade Journal Entry", layout="centered")

st.title("🧾 Trade Journal Entry Form")

# Basic info
with st.form("trade_entry"):
    st.subheader("Trade Details")

    date = st.date_input("Date")
    pair = st.text_input("Pair (e.g., EUR/USD)")
    direction = st.selectbox("Direction", ["Long", "Short"])
    entry = st.number_input("Entry Price", step=0.0001, format="%.5f")
    sl = st.number_input("SL Price", step=0.0001, format="%.5f")
    tp = st.number_input("TP Price", step=0.0001, format="%.5f")
    risk = st.number_input("Risk (%)", step=0.1, min_value=0.1, max_value=10.0)
    result = st.selectbox("Trade Result", ["Open", "Win", "Loss", "Breakeven"])
    rr = st.number_input("Reward:Risk Ratio (optional)", step=0.1, format="%.2f")
    

    st.subheader("Entry Criteria Checklist")
    flow_1d = st.checkbox("1D Flow Aligned")
    liq_sweep_4h = st.checkbox("4H Liquidity Sweep")
    fractal_break_4h = st.checkbox("4H Fractal Break")
    pd_zone_4h = st.checkbox("4H Premium/Discount Rejection")
    fractal_1d_alignment = st.checkbox("4H Fractal Same in 1D Flow")

    comments = st.text_area("Comments / Observations")

    submitted = st.form_submit_button("💾 Submit Trade")

    if submitted:
        criteria = {
            "1D Flow Aligned": flow_1d,
            "4H Liquidity Sweep": liq_sweep_4h,
            "4H Fractal Break": fractal_break_4h,
            "4H Premium/Discount Rejection": pd_zone_4h,
            "4H Fractal Same in 1D Flow": fractal_1d_alignment
        }

        score, compromised, quality = calculate_score(criteria)
        trade_id = get_next_trade_id()

        trade_data = {
            "trade_id": trade_id,
            "date": date,
            "pair": pair,
            "direction": direction,
            "entry_price": entry,
            "sl_price": sl,
            "tp_price": tp,
            "risk_percent": risk,
            "result": result,
            "rr_ratio": rr,
            "flow_1d": flow_1d,
            "liq_sweep_4h": liq_sweep_4h,
            "fractal_break_4h": fractal_break_4h,
            "pd_zone_4h": pd_zone_4h,
            "fractal_1d_alignment": fractal_1d_alignment,
            "score": score,
            "compromised_criteria": compromised,
            "quality_label": quality,
            "comments": comments
        }

        save_trade(trade_data)

        st.success(f"✅ Trade {trade_id} saved successfully! (Score: {score} - {quality})")
        st.write("**Compromised Conditions:**", compromised)




