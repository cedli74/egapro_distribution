from flask import Flask, jsonify
import csv
import os

app = Flask(__name__)

def load_data():
    data = []
    csv_path = os.path.join(os.path.dirname(__file__), "../data/index-egalite-fh-utf8.csv")
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

data = load_data()

@app.route("/api/v1/entreprises", methods=["GET"])
def get_entreprises():
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
