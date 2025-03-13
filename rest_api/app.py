from flask import Flask, jsonify
from flasgger import Swagger, swag_from
import csv

app = Flask(__name__)
Swagger(app)

def load_data():
    data = []
    csv_path = "/app/data/index-egalite-fh-utf8.csv"
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

@app.route("/api/v1/entreprises", methods=["GET"])
@swag_from({
    "tags": ["Entreprises"],
    "description": "Retourne la liste de toutes les entreprises",
    "responses": {
        "200": {
            "description": "Liste des entreprises"
        }
    }
})
def get_entreprises():
    data = load_data()
    return jsonify(data)

@app.route("/api/v1/entreprises/<siren>", methods=["GET"])
@swag_from({
    "tags": ["Entreprises"],
    "parameters": [
        {
            "name": "siren",
            "in": "path",
            "type": "string",
            "required": True,
            "description": "Numéro SIREN de l'entreprise"
        }
    ],
    "responses": {
        "200": {
            "description": "Données de l'entreprise"
        },
        "404": {
            "description": "Entreprise non trouvée"
        }
    }
})
def get_entreprise_by_siren(siren):
    data = load_data()
    entreprise = next((e for e in data if e['siren'] == siren), None)
    if entreprise:
        return jsonify(entreprise)
    else:
        return jsonify({"message": "Entreprise non trouvée"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
