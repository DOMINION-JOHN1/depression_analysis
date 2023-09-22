import pickle
import sklearn
import streamlit as st
from scipy.sparse import csr_matrix  # Import csr_matrix from scipy.sparse

# Load the model from the pickle file
with open('depression_analyzer.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Create a Streamlit web app
st.title("Depression Analyzer")

# Define a function for making predictions
def predict_depression(text):
    try:
        # Make predictions using the loaded model
        prediction = model.predict([text])[0]
        return prediction
    except Exception as e:
        return str(e)

# Create a text input for user input
user_input = st.text_input("Enter text for depression prediction:")

# Create a button to trigger the prediction
if st.button("Predict"):
    if user_input:
        prediction = predict_depression(user_input)
        st.write(f"Prediction: {prediction}")
    else:
        st.write("Please enter text for prediction.")

# Run the Streamlit app
if __name__ == '__main__':
    st.run()
