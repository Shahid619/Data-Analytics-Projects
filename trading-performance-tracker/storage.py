# storage.py
import gspread
import streamlit as st

# --- Google Sheets setup ---
service_account_info = st.secrets["gcp"]  # No need to convert to dict—it's already one
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
client = gspread.service_account_from_dict(service_account_info, scopes=scopes)
# Open your sheet
sheet = client.open_by_key("1_ONSYjb4pjVRMAjCIXAEAkvrU4qHGFkY_nbIIf3MnKw").sheet1
# No replace/strip needed—the multiline TOML handles formatting

# -------------------------- (rest of your code remains unchanged)
def get_next_trade_id():
    data = sheet.get_all_records()
    if not data:
        return 1  # First trade
    last_trade = data[-1]["trade_id"]
    return int(last_trade) + 1

def save_trade(trade_data):
    row = [
        trade_data.get("trade_id"),
        str(trade_data.get("date")),
        trade_data.get("pair"),
        trade_data.get("direction"),
        trade_data.get("entry_price"),
        trade_data.get("sl_price"),
        trade_data.get("tp_price"),
        trade_data.get("risk_percent"),
        trade_data.get("result"),
        trade_data.get("rr_ratio"),
        trade_data.get("trade_link"),
        trade_data.get("flow_1d"),
        trade_data.get("liq_sweep_4h"),
        trade_data.get("fractal_break_4h"),
        trade_data.get("pd_zone_4h"),
        trade_data.get("fractal_1d_alignment"),
        trade_data.get("score"),
        ", ".join(trade_data.get("compromised_criteria", [])),
        trade_data.get("quality_label"),
        trade_data.get("comments"),
    ]
    sheet.append_row(row, value_input_option="RAW")



