from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Load the model pipeline..
model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

class TextInput(BaseModel):
    text: list[str]

@app.post("/predict/")
async def predict(input: TextInput):
    if not input.text:
        raise HTTPException(status_code=400, detail="Text input is required.")
    predictions = model(input.text)
    return {"predictions": predictions}
