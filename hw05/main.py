from fastapi import FastAPI
import pickle

# Load your pre-trained pipeline
with open("pipeline_v1.bin", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

@app.post("/predict")
def predict(client: dict):
    proba = model.predict_proba([client])[0, 1]
    return {"probability": float(proba)}
