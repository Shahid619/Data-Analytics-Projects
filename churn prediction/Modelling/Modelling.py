import pandas as pd
df = pd.read_csv('churn_final_dataset.csv')

from sklearn.model_selection import train_test_split

X = df.drop(columns=['churn'])
y = df['churn']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

categorical_cols = X.select_dtypes(include='object').columns
numerical_cols = X.select_dtypes(exclude='object').columns

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(drop='first', handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ]
)

log_model = Pipeline(steps=[
    ('preprocessing', preprocessor),
    ('model', LogisticRegression(max_iter=1000))
])

log_model.fit(X_train, y_train)

from sklearn.metrics import classification_report, roc_auc_score

y_pred = log_model.predict(X_test)
y_proba = log_model.predict_proba(X_test)[:, 1]

# print(classification_report(y_test, y_pred))
# print("ROC-AUC:", roc_auc_score(y_test, y_proba))


# checking leakage  ===================================

df.corr(numeric_only=True)['churn'].sort_values(ascending=False)
leakage_cols = [
    'status', 'account_status', 'churn_date',
    'end_date', 'is_active'
]

X_safe = df.drop(columns=['churn'] + leakage_cols, errors='ignore')
import numpy as np

y_random = np.random.permutation(y)

log_model.fit(X_train, y_random[:len(X_train)])
y_rand_pred = log_model.predict(X_test)

print(classification_report(y_test, y_rand_pred))
