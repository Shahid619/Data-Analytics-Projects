import pandas as pd
import numpy as np

# =====================================================
# STEP 0 — LOAD RAW DATA
# =====================================================

df = pd.read_csv(
    "churn_cleaned.csv",
    parse_dates=[
        "Learner SignUp DateTime",
        "Apply Date",
        "Opportunity Start Date",
        "Opportunity End Date",
        "Entry created at",
        "Date of Birth"
    ]
)

print("Initial shape:", df.shape)

# =====================================================
# STEP 1 — DROP CORRUPTED / USELESS COLUMNS
# =====================================================

df = df.drop(columns=["First Name"], errors="ignore")

# =====================================================
# STEP 2 — LIFECYCLE VALIDATION (HARD RULES)
# =====================================================

# Rule 1: Signup <= Apply
df = df[
    (df["Learner SignUp DateTime"].isna()) |
    (df["Apply Date"].isna()) |
    (df["Learner SignUp DateTime"] <= df["Apply Date"])
]

# Rule 2: Apply <= Start
df = df[
    (df["Apply Date"].isna()) |
    (df["Opportunity Start Date"].isna()) |
    (df["Apply Date"] <= df["Opportunity Start Date"])
]

# Rule 3: Start <= End
df = df[
    (df["Opportunity Start Date"].isna()) |
    (df["Opportunity End Date"].isna()) |
    (df["Opportunity Start Date"] <= df["Opportunity End Date"])
]

# =====================================================
# STEP 3 — STATUS ↔ DATE CONSISTENCY
# =====================================================

# Rejected learners must not have start/end dates
rejected_mask = df["Status Description"].str.lower() == "rejected"
df = df[~(
    rejected_mask &
    (
        df["Opportunity Start Date"].notna() |
        df["Opportunity End Date"].notna()
    )
)]

# Started / Team Allocated must have start date
valid_started = df["Status Description"].str.lower().isin(
    ["started", "team allocated"]
)

df = df[~(
    valid_started &
    df["Opportunity Start Date"].isna()
)]

# =====================================================
# STEP 4 — KEEP ONLY CHURN-ELIGIBLE LEARNERS
# =====================================================

df = df[
    df["Status Description"].str.lower().isin(
        ["started", "team allocated"]
    )
]

print("After churn-eligible filtering:", df.shape)

# =====================================================
# STEP 5 — CREATE SURROGATE LEARNER ID
# =====================================================

df["learner_surrogate_id"] = (
    df["Date of Birth"].astype(str) + "_" +
    df["Gender"].astype(str) + "_" +
    df["Country"].astype(str)
)

# =====================================================
# STEP 6 — DEDUPLICATION (MOST ADVANCED STATUS WINS)
# =====================================================

status_rank = {
    "rejected": 0,
    "applied": 1,
    "team allocated": 2,
    "started": 3
}

df["status_rank"] = (
    df["Status Description"]
    .str.lower()
    .map(status_rank)
)

df = (
    df.sort_values("status_rank", ascending=False)
      .drop_duplicates(
          subset=["learner_surrogate_id", "Opportunity Id"],
          keep="first"
      )
)

print("After deduplication:", df.shape)

# =====================================================
# STEP 7 — CATEGORICAL NORMALIZATION
# =====================================================

# Gender
df["Gender"] = df["Gender"].str.strip().str.title()
df = df[df["Gender"].isin(["Male", "Female"])]

# Country
df["Country"] = df["Country"].str.strip().str.title()

# Major bucketization
def major_bucket(x):
    if pd.isna(x):
        return "Other"
    x = x.lower()
    if "computer" in x or "software" in x or "it" in x:
        return "CS / IT"
    if "engineer" in x:
        return "Engineering"
    if "business" in x or "management" in x:
        return "Business"
    return "Other"

df["Major_Bucket"] = df["Current/Intended Major"].apply(major_bucket)

# =====================================================
# STEP 8 — FEATURE ENGINEERING (ANALYTICS SIGNALS)
# =====================================================

df["signup_to_apply_days"] = (
    df["Apply Date"] - df["Learner SignUp DateTime"]
).dt.days

df["apply_to_start_days"] = (
    df["Opportunity Start Date"] - df["Apply Date"]
).dt.days

df["opportunity_duration_days"] = (
    df["Opportunity End Date"] - df["Opportunity Start Date"]
).dt.days

df["learner_age_at_signup"] = (
    (df["Learner SignUp DateTime"] - df["Date of Birth"])
    .dt.days // 365
)

# =====================================================
# STEP 9 — FINAL CHURN LABEL (STATUS-BASED)
# =====================================================
# IMPORTANT:
# Engagement data is missing.
# Churn is inferred using final learner status.

df["churn"] = np.where(
    df["Status Description"].str.lower() == "started",
    0,  # Retained
    1   # Churned
)

df["lifecycle_status"] = np.where(
    df["churn"] == 1,
    "Churned",
    "Retained"
)

# =====================================================
# STEP 10 — FINAL SANITY CHECKS
# =====================================================

print("\nFinal churn distribution (%):")
print(df["lifecycle_status"].value_counts(normalize=True) * 100)

print("\nFinal shape:", df.shape)

# =====================================================
# STEP 11 — SAVE FINAL DATASET
# =====================================================

df.to_csv("churn_final_dataset.csv", index=False)
print("\n✅ Final churn dataset saved as 'churn_final_dataset.csv'")
