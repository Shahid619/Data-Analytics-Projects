# FX Trade Journal & Analytics Dashboard

## Project Overview
This project is an **end-to-end trade tracking and analytics system** for FX trading. It allows a user to log trades, track performance, and visualize trading insights via a dashboard.

The project consists of two main components:

1. **Trade Input Web App (Streamlit)**
   - Web form to enter trade details:
     - Pair, Direction, Entry Price, SL, TP, Risk%, Result, R:R ratio, Entry Criteria (5-point checklist), Comments
   - Auto-calculates:
     - Trade Score (0–100 based on criteria)
     - Quality Label (Perfect, High, Average, Weak)
     - Compromised Conditions
   - Saves data in a CSV (`trades.csv`) for analytics.

2. **Power BI Dashboard**
   - Fetches trade data from CSV and displays:
     - Page 1: KPI Cards + PnL over time (line chart)
     - Page 2: Main dashboard with KPIs (Total Trades, Avg RR, Win Rate, PnL by Result) + Graphs (Line, Pie, PnL by Result)
     - Page 3: Detailed tables (Heatmap, Trade IDs + Confidence) + PnL per trade graph

---

## Features
- **Trade Scoring System:** Assigns a score based on 5 key conditions to measure trade quality.
- **Automatic Quality Labels:** Perfect Trade, High Quality, Average Setup, Weak Trade.
- **Comprehensive Dashboard:** Multiple pages with KPIs, charts, tables, and filters.
- **Dynamic Insights:** PnL tracking, quality distribution, trade outcome analysis.
- **CSV-based storage:** Simple and flexible for future upgrades to SQLite or databases.

---

## Challenges Faced & How I Handled Them
1. **Data Consistency**
   - Issue: Trade input can be inconsistent (missing fields, incorrect formats)
   - Solution: Added validation in Streamlit form, ensured all fields mandatory.

2. **Score Calculation Logic**
   - Issue: Multiple conditions with different combinations for trade quality
   - Solution: Created modular scoring function with clear mapping from criteria to score and quality label.

3. **CSV Storage & Auto-Increment IDs**
   - Issue: Need unique trade IDs and append without losing data
   - Solution: Implemented function to auto-generate incremental trade IDs and append new rows safely.

4. **Dashboard Insights**
   - Issue: Displaying multiple KPIs, charts, and tables in a clean and interactive way
   - Solution: Organized Power BI into 3 pages, used slicers for filtering, applied consistent visual style.

5. **End-to-End Integration**
   - Issue: Linking Streamlit input to Power BI dashboard
   - Solution: Used CSV as a central data source, enabling seamless updates with each trade entry.

---

## Tech Stack
- **Frontend & Data Input:** Streamlit (Python)
- **Data Storage:** CSV (future upgrade to SQLite)
- **Analytics & Visualization:** Power BI
- **Libraries Used (Python):** pandas, streamlit

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/username/fx-trade-journal.git

--------------------------

dependencies:  pip install -r requirements.txt
RUn app :  streamlit run app.py

-----------------Repo Structure: 
trading_journal/
│
├── app.py                 # Streamlit trade input form
├── utils/
│    ├── scoring.py        # Trade scoring logic
│    └── storage.py        # CSV read/write logic
├── data/
│    └── trades.csv        # Trade journal data
├── README.md              # This file
└── requirements.txt       # Python dependencies
