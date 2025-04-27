import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv("data/crop_prices.csv")

# Prepare data for training
data['month'] = pd.to_datetime(data['month'])
data['month_num'] = data['month'].dt.month
X = data[['month_num']]
y = data['price_per_kg']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("models/price_prediction.pkl", "wb") as f:
    pickle.dump(model, f)
