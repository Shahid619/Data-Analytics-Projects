# 🏥 Hospital Readmission Analytics Dashboard (Power BI)

### 📘 Overview
This project analyzes hospital patient data to identify key factors driving **readmissions within 30 days**.  
Using Power BI, I built an **interactive dashboard** that helps healthcare professionals track readmission trends, analyze patient demographics, and detect clinical risk factors.

**Dataset:** [Hospital Readmission Prediction (Synthetic Dataset)](https://www.kaggle.com/datasets/)  
**Records:** 30,000  
**Features:** 11 (clinical + demographic)  
**Target Variable:** `readmitted_30_days` (Yes/No)

---

## 🎯 Project Objective
To understand and visualize which patient segments are most at risk of being readmitted within 30 days of discharge — helping hospitals improve discharge planning and reduce costs.

---

## ⚙️ Tools & Skills Used
- **Power BI Desktop**
- **Power Query** (Data Cleaning & Transformation)
- **DAX** (Custom KPIs and Calculated Columns)
- **Data Modeling** (Single-table model)
- **Data Visualization & Storytelling**
- **Domain:** Healthcare Analytics

---

## 📊 Dashboard KPIs

| Metric | Description | DAX Logic |
|---------|--------------|------------|
| **Total Patients** | Count of all patients | `COUNTROWS(HospitalData)` |
| **Readmissions (30 Days)** | Count of patients readmitted | `CALCULATE(COUNTROWS(HospitalData), HospitalData[readmitted_30_days]="Yes")` |
| **Readmission Rate (%)** | % of total patients readmitted | `DIVIDE([Readmissions],[Total Patients],0)` |
| **Average Stay (Days)** | Avg. of `time_in_hospital` | `AVERAGE(HospitalData[time_in_hospital])` |
| **Average Medications** | Avg. of `num_medications` | `AVERAGE(HospitalData[num_medications])` |

---

## 📈 Insights Summary

- **Total Patients:** 30,000  
- **Readmissions:** 3.67K (~12%)  
- **Avg. Stay:** 6 Days | **Avg. Meds:** 5  

**Demographic Trends**
- Readmission Rate:  
  - Male → 12.3%  
  - Female → 12.1%  
  - Other → 12.3%
- Highest Risk Age Group → 20–39 (12.5%)  
- Lowest Risk Age Group → 80+ (11.6%)

**Clinical Trends**
- Short stays (1 day) have **highest readmission risk (~13.2%)**
- Peak readmission rate at **ages 25–35 (~15–17%)**
- Longer hospital stays reduce readmission probability

---

## 📋 Dashboard Pages

1. **Overview Page**
   - KPIs: Total Patients, Readmission %, Avg Stay, Avg Meds
   - Donut Chart: Readmission by Gender
   - Bar Chart: Readmission by Age Group
   - Line Chart: Readmission vs Stay Duration

2. **Clinical Risk Factors**
   - Scatter: Time in Hospital vs Medications
   - Bar: Readmission by Admission Type
   - Matrix: Diagnosis Count × Admission Type × Readmission Rate

3. **Risk Segmentation**
   - Matrix: Age × Gender × Readmission %
   - Table: Top 10 High-Risk Segments
   - Gauge: Actual vs Target Readmission Rate (12%)

---

## 🧠 Key Learning Outcomes
- Learned **data storytelling** for healthcare analytics
- Designed **KPI-focused dashboards** with drill-through filters
- Applied **DAX for performance metrics**
- Translated data into **actionable insights** for hospital management
---

## 🏁 Next Steps
Next phase will extend this project by applying **Logistic Regression** to predict patient readmission risk and integrate model results back into Power BI.
