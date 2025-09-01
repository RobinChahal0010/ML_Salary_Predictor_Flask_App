import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
df = pd.read_csv("ds_salaries.csv")

# Keep only necessary columns
df = df[['experience_level', 'employment_type', 'job_title', 
         'employee_residence', 'company_size', 'salary_in_usd']]

# Features and target
X = df.drop("salary_in_usd", axis=1)
y = df["salary_in_usd"]

# Categorical columns
categorical_features = ['experience_level', 'employment_type', 
                        'job_title', 'employee_residence', 'company_size']

# Column transformer
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

# Pipeline
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model.fit(X_train, y_train)

# Evaluate
r2 = model.score(X_test, y_test)
print(f"✅ Model trained. R² Score: {r2:.4f}")

# Save model
joblib.dump(model, "model/salary_model.pkl")
print("💾 Model saved at model/salary_model.pkl")
