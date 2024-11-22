import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, confusion_matrix
import statsmodels.api as sm
import matplotlib.pyplot as plt

# ==============================
# Directory to Save Outputs
# ==============================
output_dir = "../outputs"
os.makedirs(output_dir, exist_ok=True)

# ==============================
# Data Loading and Preprocessing
# ==============================
# Load the cleaned dataset
file_path_cleaned = "../data/FL_HeavyMetalMaster_111824_MissingRemoved.csv"
df_cleaned = pd.read_csv(file_path_cleaned)

# Define biologically relevant metals and covariates
metals_of_interest = ["Lead", "Cadmium", "Zinc", "Manganese"]
covariates = ["Sex", "Age"]
required_columns = ["Disease"] + covariates + metals_of_interest

# Ensure required columns are present
assert set(required_columns).issubset(df_cleaned.columns), "Missing required columns in the dataset."

# Map 'M' to 1 (Male) and 'F' to 0 (Female) in the Sex column
df_cleaned["Sex"] = df_cleaned["Sex"].map({"M": 1, "F": 0})
assert df_cleaned["Sex"].notnull().all(), "Missing or unmapped values in 'Sex'."

# Prepare feature matrix and target variable
X = df_cleaned[covariates + metals_of_interest]
y = df_cleaned["Disease"]

# Standardize continuous features (Age and metals)
columns_to_standardize = metals_of_interest + ["Age"]
X[columns_to_standardize] = (X[columns_to_standardize] - X[columns_to_standardize].mean()) / \
                             X[columns_to_standardize].std()

# ==============================
# Logistic Regression
# ==============================
# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Add constant to both train and test sets
X_train_const = sm.add_constant(X_train)
X_test_const = sm.add_constant(X_test)

# Fit the model using statsmodels
logit_model = sm.Logit(y_train, X_train_const).fit()
print(logit_model.summary())

# Predict on the test set
y_pred_proba = logit_model.predict(X_test_const)
y_pred = (y_pred_proba >= 0.5).astype(int)

# Evaluate model performance
roc_auc = roc_auc_score(y_test, y_pred_proba)
conf_matrix = confusion_matrix(y_test, y_pred)
print(f"ROC-AUC: {roc_auc:.2f}")
print("Confusion Matrix:")
print(conf_matrix)

# Save Confusion Matrix as a CSV
conf_matrix_path = os.path.join(output_dir, "confusion_matrix_model4.csv")
pd.DataFrame(conf_matrix, index=["Actual_0", "Actual_1"], columns=["Predicted_0", "Predicted_1"]).to_csv(conf_matrix_path)
print(f"Confusion matrix saved to {conf_matrix_path}.")
