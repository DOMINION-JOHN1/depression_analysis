import pickle
import sklearn
from fastapi import FastAPI, HTTPException # Assuming 'FastAPI' is from 'fastapi' module, not 'main'
# Load the model from the pickle file
with open('depression_analyzer.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
# Create a FastAPI instance
app = FastAPI()
# Define a function for making predictions
@app.post("/predict")
async def predict_depression(text: dict):
    try:
        input_text = text.get("text")
        if input_text is None:
            raise HTTPException(status_code=400, detail="Missing 'text' field in request")
        # Make predictions using the loaded model
        prediction = model.predict([input_text])[0]
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)