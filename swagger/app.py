from flask import Flask, jsonify
from flasgger import Swagger, swag_from

app = Flask(__name__)
Swagger(app)

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
    # Cette route est un proxy pour la documentation, pas besoin de logique ici
    return jsonify({"message": "Liste des entreprises"})

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
            "description": "Données de l'entreprise",
            "examples": {
                "application/json": {
                    "siren": "123456789",
                    "nom": "Entreprise Exemple",
                    "score_egalite": 95
                }
            }
        },
        "404": {
            "description": "Entreprise non trouvée"
        }
    }
})
def get_entreprise_by_siren(siren):
    # Cette route est un proxy pour la documentation, pas besoin de logique ici
    return jsonify({"message": "Données de l'entreprise"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
