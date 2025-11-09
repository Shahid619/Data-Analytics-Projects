# Power BI Sales Dashboard – End-to-End Data Pipeline & Visualization

![Dashboard Preview](dashboard_preview.png)

## 📊 Project Overview
This **Power BI Sales Dashboard** provides a comprehensive view of sales performance, profitability, and customer segmentation for a retail business. Built as part of a **complete data analytics pipeline**, it demonstrates real-world skills in:
- Data extraction & cleaning
- ETL process design
- Interactive dashboard development in **Power BI**
- Insight-driven reporting

---

## 📈 Key Metrics
| Metric           | Value       |
|------------------|-------------|
| **Total Sales**  | **$2M**     |
| **Total Profit** | **$286K**   |
| **Profit Margin**| **12.5%**   |

---

## 📊 Dashboard Highlights

### 1. **Monthly Sales Trend**
- Line chart showing sales evolution across 12 months
- Notable peak in **September**
- Slight dip in **November**

### 2. **Sales by Segment**
- **Consumer**: $1.16M (58%)
- **Corporate**: $710K (35.5%)
- **Home Office**: $430K (21.5%)

### 3. **Sales by Shipping Mode**
- **Standard Class** dominates with **$1.36M**
- **Same Day** shipping: $130K (fast but low volume)

### 4. **Sales by Category (Pie Chart)**
- **Technology**: 36.4% ($836K)
- **Furniture**: 31.3% ($719K)
- **Office Supplies**: 32.3% ($742K)

---

## 🛠️ Tech Stack
- **Power BI Desktop** – Dashboard & DAX calculations
- **Excel / CSV** – Sample dataset
- **DAX** – Profit margin, YoY growth, dynamic measures
- **GitHub** – Version control & project hosting

---

## 🚀 Pipeline Overview
```mermaid
graph LR
    A[Raw Sales Data] --> B[Data Cleaning]
    B --> C[Power BI Import]
    C --> D[Data Modeling]
    D --> E[DAX Calculations]
    E --> F[Interactive Dashboard]
    F --> G[Insight Generation]
