import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Title
st.title("🌸 Iris Flower Prediction App")

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Sidebar input
st.sidebar.header("Input Features")

def user_input():
    sepal_length = st.sidebar.slider("Sepal Length", 4.0, 8.0, 5.4)
    sepal_width = st.sidebar.slider("Sepal Width", 2.0, 4.5, 3.4)
    petal_length = st.sidebar.slider("Petal Length", 1.0, 7.0, 1.3)
    petal_width = st.sidebar.slider("Petal Width", 0.1, 2.5, 0.2)

    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input()

# Show input
st.subheader("User Input")
st.write(input_df)

# Prediction
prediction = model.predict(input_df)
probability = model.predict_proba(input_df)

# Output
st.subheader("Prediction")
st.write(iris.target_names[prediction][0])

st.subheader("Prediction Probability")
st.write(pd.DataFrame(probability, columns=iris.target_names))
