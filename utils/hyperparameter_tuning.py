from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import pandas as pd

# Load prepared data
df = pd.read_csv('data/prepared_data.csv')

# Assuming the target variable is 'is_malicious' (change as needed)
X = df.drop(columns=['is_malicious'])
y = df['is_malicious']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the RandomForest model
model = RandomForestClassifier(random_state=42)

# Define the parameter grid for tuning
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

# Initialize GridSearchCV with the Random Forest model
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)

# Fit the model with the best parameters
grid_search.fit(X_train, y_train)

# Get the best parameters and the best score from the grid search
print(f"Best Parameters: {grid_search.best_params_}")
print(f"Best Score: {grid_search.best_score_}")

# Use the best estimator
best_model = grid_search.best_estimator_

# Save the best model
joblib.dump(best_model, 'models/random_forest_best_model.pkl')
print("Best model saved successfully!")
print("Best Parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)
