# storage.py
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

# --- Google Sheets setup ---
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

service_account_info = st.secrets["gcp"]
creds_dict = dict(service_account_info)

# Fix key formatting (if needed)
creds_dict["private_key"] = creds_dict["private_key"].replace("\\n", "\n").strip()

# Authorize
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

# Open your sheet
sheet = client.open_by_key("1_ONSYjb4pjVRMAjCIXAEAkvrU4qHGFkY_nbIIf3MnKw").sheet1

# --------------------------
# Get the next trade ID
# --------------------------
def get_next_trade_id():
    data = sheet.get_all_records()
    if not data:
        return 1  # First trade
    last_trade = data[-1]["trade_id"]
    return int(last_trade) + 1

# --------------------------
# Save a trade entry
# --------------------------
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


