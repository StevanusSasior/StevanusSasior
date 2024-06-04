
import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load the Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.DataFrame(iris.target, columns=['target'])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train.values.ravel())

# Streamlit app
st.title("Iris Flower Species Classification")

st.write('''
This app uses a RandomForestClassifier to classify Iris flower species based on their features.
''')

# Sidebar for user input
st.sidebar.header('User Input Features')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', float(X['sepal length (cm)'].min()), float(X['sepal length (cm)'].max()), float(X['sepal length (cm)'].mean()))
    sepal_width = st.sidebar.slider('Sepal width', float(X['sepal width (cm)'].min()), float(X['sepal width (cm)'].max()), float(X['sepal width (cm)'].mean()))
    petal_length = st.sidebar.slider('Petal length', float(X['petal length (cm)'].min()), float(X['petal length (cm)'].max()), float(X['petal length (cm)'].mean()))
    petal_width = st.sidebar.slider('Petal width', float(X['petal width (cm)'].min()), float(X['petal width (cm)'].max()), float(X['petal width (cm)'].mean()))
    data = {'sepal length (cm)': sepal_length,
            'sepal width (cm)': sepal_width,
            'petal length (cm)': petal_length,
            'petal width (cm)': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Combine user input with the complete dataset for scaling (if needed)
iris_data = pd.concat([input_df, X], axis=0)

# Predict the class
prediction = clf.predict(input_df)
prediction_proba = clf.predict_proba(input_df)

# Display results
st.subheader('Prediction')
iris_species = ['Setosa', 'Versicolour', 'Virginica']
st.write(iris_species[prediction[0]])

st.subheader('Prediction Probability')
st.write(prediction_proba)
