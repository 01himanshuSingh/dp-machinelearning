from sklearn.linear_model import LinearRegression
import numpy as np

# Simple training data
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict
prediction = model.predict([[5]])

print("Prediction:", prediction[0])
