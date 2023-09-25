import pickle
import sklearn
from fastapi import FastAPI  # Assuming 'FastAPI' is from 'fastapi' module, not 'main'

# Load the model from the pickle file
with open('depression_analyzer.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Create a FastAPI instance
app = FastAPI()

# Define a function for making predictions
@app.post("/predict")
async def predict_depression(text: str):
    try:
        # Make predictions using the loaded model
        prediction = model.predict([text])[0]
        return {"prediction": prediction}
    except Exception as e:
        return {"error": str(e)}
