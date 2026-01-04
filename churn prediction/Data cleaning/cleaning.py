import pandas as pd
import numpy as np

df = pd.read_csv("Cleaned_v1.csv")

# print(df.shape)
# print(df.head())


# First Name is numeric & unusable → drop
df = df.drop(columns=["First Name"], errors="ignore")
# print(df)


# Convert date columns to datetime (CRITICAL)
date_cols = [
    "Learner SignUp DateTime",
    "Apply Date",
    "Opportunity Start Date",
    "Opportunity End Date",
    "Entry created at",
    "Date of Birth"
]

for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors="coerce")

# print(df.head())


# Remove lifecycle-invalid records
df = df[
    (df["Learner SignUp DateTime"].isna()) |
    (df["Apply Date"].isna()) |
    (df["Learner SignUp DateTime"] <= df["Apply Date"])
]
# print(df.head())

# Apply after Start
df = df[
    (df["Apply Date"].isna()) |
    (df["Opportunity Start Date"].isna()) |
    (df["Apply Date"] <= df["Opportunity Start Date"])
]
# print(df)


# Start after End
df = df[
    (df["Opportunity Start Date"].isna()) |
    (df["Opportunity End Date"].isna()) |
    (df["Opportunity Start Date"] <= df["Opportunity End Date"])
]


# Rejected users must NOT have start/end dates
rejected_mask = df["Status Description"].str.lower() == "rejected"

df = df[~(
    rejected_mask &
    (
        df["Opportunity Start Date"].notna() |
        df["Opportunity End Date"].notna()
    )
)]
# print(df)


# Started / Team Allocated MUST have start date
valid_status = ["started", "team allocated"]

df = df[
    ~(
        df["Status Description"].str.lower().isin(valid_status) &
        df["Opportunity Start Date"].isna()
    )
]
# print(df)

# Keep only churn-eligible records
df = df[
    df["Status Description"].str.lower().isin(["started", "team allocated"])
]
# print(df)

# Create surrogate learner ID
df["learner_surrogate_id"] = (
    df["Date of Birth"].astype(str) + "_" +
    df["Gender"].astype(str) + "_" +
    df["Country"].astype(str)
)
# print(df)


# Status hierarchy (keep most advanced)
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
# print(df)

# Deduplicate
df = (
    df.sort_values("status_rank", ascending=False)
      .drop_duplicates(
          subset=["learner_surrogate_id", "Opportunity Id"],
          keep="first"
      )
)
# print(df)


# Normalize categorical columns
df["Gender"] = df["Gender"].str.strip().str.title()
df = df[df["Gender"].isin(["Male", "Female"])]


# Country
df["Country"] = df["Country"].str.strip().str.title()

# Major (bucketization)
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


# Feature engineering (needed for churn logic)
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
# print(df)


# Final sanity checks
# assert (df["apply_to_start_days"] >= 0).all()
# assert (df["signup_to_apply_days"] >= 0).all()



# Save cleaned dataset
df.to_csv("churn_cleaned.csv", index=False)
# print("Step 2 completed. Clean dataset saved.")
