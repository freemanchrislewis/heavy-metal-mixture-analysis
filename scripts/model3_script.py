import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, confusion_matrix
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# ==============================
# Data Loading and Preprocessing
# ==============================
# Load the cleaned dataset
file_path_cleaned = "../data/FL_HeavyMetalMaster_111824_MissingRemoved.csv"
df_cleaned = pd.read_csv(file_path_cleaned)

# Define updated biologically relevant metals (e.g., after removing Nickel)
biologically_relevant_metals = ["Mercury", "Lead", "Cadmium", "Zinc", "Manganese"]

# Ensure required columns are present
required_columns = ["Disease", "Sex", "Age"] + biologically_relevant_metals
assert set(required_columns).issubset(df_cleaned.columns), "Missing required columns in the dataset."

# Map 'M' to 1 (Male) and 'F' to 0 (Female) in the Sex column
df_cleaned["Sex"] = df_cleaned["Sex"].map({"M": 1, "F": 0})
assert df_cleaned["Sex"].notnull().all(), "Missing or unmapped values in 'Sex'."

# Prepare the feature matrix
X = df_cleaned[["Sex", "Age"] + biologically_relevant_metals]
y = df_cleaned["Disease"]

# Standardize continuous features (Age and metals)
columns_to_standardize = biologically_relevant_metals + ["Age"]
X[columns_to_standardize] = (X[columns_to_standardize] - X[columns_to_standardize].mean()) / \
                             X[columns_to_standardize].std()

# ==============================
# VIF Calculation
# ==============================
def calculate_vif(dataframe):
    vif_data = pd.DataFrame()
    vif_data["Feature"] = dataframe.columns
    vif_data["VIF"] = [variance_inflation_factor(dataframe.values, i) for i in range(dataframe.shape[1])]
    return vif_data

vif_df = calculate_vif(X)
print("Updated VIF for main effects:")
print(vif_df)

# ==============================
# Logistic Regression
# ==============================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the model using statsmodels for detailed output
X_train_const = sm.add_constant(X_train)
logit_model = sm.Logit(y_train, X_train_const).fit()
print(logit_model.summary())

# Predict on the test set
X_test_const = sm.add_constant(X_test)
y_pred_proba = logit_model.predict(X_test_const)
y_pred = (y_pred_proba >= 0.5).astype(int)

# Evaluate model performance
roc_auc = roc_auc_score(y_test, y_pred_proba)
conf_matrix = confusion_matrix(y_test, y_pred)
print(f"ROC-AUC: {roc_auc:.2f}")
print("Confusion Matrix:")
print(conf_matrix)
