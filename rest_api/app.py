from flask import Flask, jsonify
import csv
import os

app = Flask(__name__)

# Données chargées au démarrage
DATA = []

def load_data():
    global DATA
    csv_path = os.path.join(os.path.dirname(__file__), "/app/data/index-egalite-fh-utf8.csv")
    
    try:
        with open(csv_path, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            DATA = [row for row in reader]

        if DATA:
            print(f"✅ {len(DATA)} entreprises chargées depuis le fichier CSV.")
            print(f"🔍 Colonnes disponibles : {list(DATA[0].keys())}")  # Vérifier les colonnes

            # Vérifier un exemple d'entreprise pour voir comment les données sont stockées
            example = DATA[0]
            print(f"📌 Exemple de ligne chargée : {example}")

    except Exception as e:
        print(f"❌ Erreur lors du chargement des données : {e}")

# Charger les données une seule fois
load_data()

def clean_string(value):
    """ Nettoie une chaîne : supprime les espaces et normalise l'encodage. """
    return str(value).strip() if value else ""

@app.route("/api/v1/entreprises/<siren>", methods=["GET"])
def get_entreprise_by_siren(siren):
    siren = clean_string(siren)  # Nettoyer le SIREN en entrée

    # Vérifier si le SIREN est bien chargé dans les données
    all_sirens = [clean_string(e.get('SIREN', '')) for e in DATA]
    
    if siren not in all_sirens:
        print(f"❌ SIREN {siren} non trouvé dans la base !")
        return jsonify({"message": "Entreprise non trouvée"}), 404

    # Recherche de l'entreprise
    entreprise = next((e for e in DATA if clean_string(e.get('SIREN', '')) == siren), None)

    if entreprise:
        print(f"✅ Entreprise trouvée pour SIREN {siren} : {entreprise['Raison Sociale']}")
        return jsonify(entreprise)
    else:
        print(f"❌ Aucune entreprise trouvée pour le SIREN : {siren}")
        return jsonify({"message": "Entreprise non trouvée"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
