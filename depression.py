import pickle
from fastapi import FastAPI, HTTPException
from fastapi.middleware.wsgi import WSGIMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

# Load the model from the pickle file
with open('depression_analyzer.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = FastAPI()

class DisableFaviconMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if request.url.path == "/favicon.ico":
            return Response(content=b"", status_code=200)
        return await call_next(request)

app.add_middleware(DisableFaviconMiddleware)

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
