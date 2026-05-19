import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("Hello Sklearn App")

X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

model = LinearRegression()
model.fit(X, y)

value = st.number_input("Enter number")

if st.button("Predict"):
    prediction = model.predict([[value]])
    st.write("Prediction:", prediction[0])
