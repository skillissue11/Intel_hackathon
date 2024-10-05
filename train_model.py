import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearnex import patch_sklearn

# Patch scikit-learn with Intel Extension
patch_sklearn()

# Load the dataset
data_path = '/kaggle/input/ibm-hr-analytics-attrition-dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv'  # Adjust the path accordingly
df = pd.read_csv(data_path)

# Encode categorical variables (save the column names after encoding)
df_encoded = pd.get_dummies(df, drop_first=True)
encoded_columns = df_encoded.columns.tolist()  # Save as a list

# Define features and target variable
X = df_encoded.drop('Attrition_Yes', axis=1)
y = df_encoded['Attrition_Yes']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model and the column names
joblib.dump(model, 'model/employee_attrition_model.joblib')
joblib.dump(encoded_columns, 'model/encoded_columns.joblib')  # Save the column names
print("Model and columns saved successfully.")
