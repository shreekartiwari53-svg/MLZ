from flask import Flask, request, jsonify
import pickle
import csv

app = Flask(__name__)

# Load model and DictVectorizer
with open("xgb_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("dv.pkl", "rb") as f:
    dv = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Make prediction
    price = model.predict(dv.transform([data]))[0]

    # Log input + prediction
    with open("predictions_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([*data.values(), price])

    return jsonify({"predicted_price": price})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

