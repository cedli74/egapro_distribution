from flask import Flask, jsonify
from flasgger import Swagger
import csv

app = Flask(__name__)
Swagger(app)

def load_data():
    data = []
    with open("../data/index-egalite-fh-utf8.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

data = load_data()

@app.route("/api/v1/entreprises", methods=["GET"])
def get_entreprises():
    """
    Récupérer la liste des entreprises
    ---
    responses:
      200:
        description: Liste des entreprises
    """
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

