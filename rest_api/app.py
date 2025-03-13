from flask import Flask, jsonify
import csv
import os

app = Flask(__name__)

# Chargement unique des données CSV au démarrage
DATA = []

def load_data():
    global DATA
    csv_path = os.path.join(os.path.dirname(__file__), "../data/index-egalite-fh-utf8.csv")
    
    try:
        with open(csv_path, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            DATA = [row for row in reader]

        if DATA:
            print(f"✅ {len(DATA)} entreprises chargées depuis le fichier CSV.")
            print(f"🔍 Colonnes disponibles : {list(DATA[0].keys())}")  # Vérifier les noms des colonnes

    except Exception as e:
        print(f"❌ Erreur lors du chargement des données : {e}")

# Charger les données une seule fois
load_data()

def clean_string(value):
    """ Nettoie une chaîne : supprime les espaces et normalise l'encodage. """
    return value.strip() if value else ""

@app.route("/api/v1/entreprises/<siren>", methods=["GET"])
def get_entreprise_by_siren(siren):
    siren = clean_string(siren)  # Nettoyer le SIREN en entrée
    entreprise = next((e for e in DATA if clean_string(e.get('SIREN', '')) == siren), None)

    if entreprise:
        print(f"✅ Entreprise trouvée pour SIREN {siren} : {entreprise['Raison Sociale']}")
        return jsonify(entreprise)
    else:
        print(f"❌ Aucune entreprise trouvée pour le SIREN : {siren}")
        return jsonify({"message": "Entreprise non trouvée"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
