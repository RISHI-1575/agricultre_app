import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
data = pd.read_csv("data/crop_recommendation.csv")

# Prepare data for training
X = data[['land_size', 'demand', 'predicted_price']]
X['demand'] = X['demand'].map({'Low': 0, 'Medium': 1, 'High': 2})  # Encode demand
y = data['crop']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open("models/crop_recommendation.pkl", "wb") as f:
    pickle.dump(model, f)
