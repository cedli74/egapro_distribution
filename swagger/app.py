from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route("/api/v1/entreprises", methods=["GET"])
def get_entreprises():
    """
    Retourne la liste des entreprises.
    ---
    responses:
      200:
        description: Liste des entreprises
    """
    return jsonify({"message": "Liste des entreprises"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
