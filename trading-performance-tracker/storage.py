import pandas as pd
import os

def get_next_trade_id(filepath="data/trades.csv"):
    """Generate next trade ID (T001, T002, ...) with safe fallback."""
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        return "T001"
    try:
        df = pd.read_csv(filepath)
        if df.empty or "trade_id" not in df.columns:
            return "T001"
        last_id = df["trade_id"].iloc[-1]
        next_num = int(last_id.replace("T", "")) + 1
        return f"T{next_num:03d}"
    except Exception:
        return "T001"

def save_trade(data, filepath="data/trades.csv"):
    """Append a new trade to the CSV."""
    df = pd.DataFrame([data])
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    if os.path.exists(filepath):
        df.to_csv(filepath, mode="a", header=False, index=False)
    else:
        df.to_csv(filepath, index=False)

