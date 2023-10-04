import pickle
import asyncio
from fastapi import FastAPI, HTTPException
import concurrent.futures
import logging

# Load the model from the pickle file
try:
    with open('depression_analyzer.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
except Exception as e:
    # Handle model loading error
    raise RuntimeError("Failed to load the model.") from e

app = FastAPI()

# Configure logging to a more appropriate level for production
logging.basicConfig(level=logging.INFO)

# Use a ThreadPoolExecutor to run predictions concurrently
executor = concurrent.futures.ThreadPoolExecutor()

@app.post("/predict")
async def predict_depression(texts: dict):
    try:
        input_texts = texts.get("texts")
        if input_texts is None:
            raise HTTPException(status_code=400, detail="Missing 'texts' field in request")

        # Combine all input texts into one string
        combined_input = " ".join(input_texts)

        # Define a function to make predictions
        def predict(input_text):
            return model.predict([input_text])[0]

        # Submit the prediction task to the ThreadPoolExecutor
        prediction = await asyncio.to_thread(predict, combined_input)
        return {"prediction": prediction}
    except Exception as e:
        # Log the error details
        logging.error(f"Prediction error: {str(e)}")

        # Return a more specific HTTPException with a 400 status code for prediction errors
        raise HTTPException(status_code=400, detail="Prediction error")
