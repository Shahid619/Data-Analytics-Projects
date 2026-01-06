import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("churn_final_dataset.csv")

# Churn rate %age
churn_rate = df["churn"].mean() * 100
print(churn_rate)

# churn count 
count_Churn = df["churn"].value_counts()
print(count_Churn)

# Churn vs Apply
ch_app=df.groupby("churn")["apply_to_start_days"].median()
print(f'churn_apply : {ch_app}')
# visual
df.boxplot(column="apply_to_start_days", by="churn")
plt.title("Apply-to-Start Delay vs Churn")
plt.suptitle("")
plt.ylabel("Days")
plt.show()


# Churn vs Signup
ch_sign=df.groupby("churn")["signup_to_apply_days"].median()
print(f'churn_signup : {ch_sign}')

df.boxplot(column="signup_to_apply_days", by="churn")
plt.title("Signup-to-Apply Delay vs Churn")
plt.suptitle("")
plt.ylabel("Days")
plt.show()

# Churn vs Opportunity
ch_oppor = df.groupby("churn")["opportunity_duration_days"].median()
print(f' churn _ opportunity : {ch_oppor}')

df.boxplot(column="opportunity_duration_days", by="churn")
plt.title("Opportunity Duration vs Churn")
plt.suptitle("")
plt.ylabel("Days")
plt.show()


# Churn by Opportunity Type
churn_by_type = (
    df.groupby("Opportunity Category")["churn"].mean().sort_values(ascending=False))
print(f' churn by opportunity type : {churn_by_type}')

churn_by_type.plot(kind="bar")
plt.title("Churn Rate by Opportunity Type")
plt.ylabel("Churn Rate")
plt.show()


# Churn by Major
Churn_Major=df.groupby("Major_Bucket")["churn"].mean().sort_values(ascending=False)
print(f' Churn by major : {Churn_Major}')


# Churn by Country
Churn_country  = df.groupby("Country")["churn"].mean().sort_values(ascending=False).head(10)
print(f'Churn by Country : {Churn_country}')
