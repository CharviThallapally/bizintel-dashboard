# model.py

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def train_model():
    df = pd.read_csv("superstore.csv", encoding='latin1')

    # Select features
    features = df[["Profit", "Discount", "Quantity"]]
    target = df["Sales"]

    # Handle any missing values (if any)
    features = features.dropna()
    target = target[features.index]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    return model
