# 🛒 E-Commerce Customer Analytics Dashboard (Power BI)

## 📊 Project Overview
This project focuses on analyzing real-world e-commerce data to uncover insights about **sales performance**, **customer behavior**, **product trends**, and **operational efficiency**.

The dataset was intentionally messy and required extensive cleaning before building analytical dashboards. The goal was to simulate an **end-to-end Data Analyst workflow** — from raw data to actionable insights.

---

## 🧹 Data Cleaning & Preparation
Performed in **Power Query** and partially in **Excel/Pandas**:
- Removed duplicate records and blank rows  
- Corrected data inconsistencies (e.g., wrong date/time formats, typos)  
- Handled missing `CustomerID` and `Description` values  
- Removed outliers in `Quantity` and `UnitPrice`  
- Created derived columns and calculated measures such as:
  - `TotalPrice = Quantity * UnitPrice`
  - `Year`, `Month` from `InvoiceDate`
  - `AOV`, `Return Rate`, and RFM metrics (Recency, Frequency, Monetary)

---

## 📈 Dashboard Pages & Insights

### **Page 1 – Sales Overview**
- KPIs: Total Sales, Total Revenue, Total Returns  
- Monthly Revenue Trend (Line Chart)  
- Revenue by Country (Map / Bar Chart)  
> *Shows sales trends and top-performing regions.*

---

### **Page 2 – Customer Insights**
- Top 10 Customers by Revenue  
- RFM Analysis (Recency, Frequency, Monetary)  
- Segmentation by Spending Category  
> *Helps understand customer loyalty, activity, and value segmentation.*

---

### **Page 3 – Product Performance**
- Top 10 Products by Revenue  
- Sales vs Returns by Product (Stacked Column)  
- Quantity Trend by Product Category  
> *Highlights best-selling items and identifies products with high return rates.*

---

### **Page 4 – Operational Insights**
- Average Order Value (AOV)  
- Average Items per Order  
- Invoices per Month  
- Returns Rate Over Time  
> *Monitors business efficiency, order sizes, and operational issues.*

---

## 🧠 Key Learnings
- Practiced **data cleaning and transformation** in Power BI  
- Designed **data model relationships** for analysis  
- Created **DAX measures** to calculate KPIs  
- Developed **interactive dashboards** for multi-level business insights  

---

## 💼 Tools Used
- **Power BI**
- **Excel / Power Query**
- **DAX**
- **Data Visualization & Storytelling**


