import pickle

with open("pipeline_v1.bin", "rb") as f:
    model = pickle.load(f)

client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

prob = model.predict_proba([client])[0, 1]
print("Probability:", prob)
