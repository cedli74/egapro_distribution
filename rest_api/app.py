from flask import Flask, jsonify
import csv
import unicodedata
import re

app = Flask(__name__)

def normalize_column_name(name):
    # Supprime les accents et les caractères spéciaux
    name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode('ASCII')
    # Remplace les espaces et les caractères non alphanumériques par des underscores
    name = re.sub(r'[^\w\s]', '', name).replace(' ', '_')
    return name

def load_data():
    data = []
    csv_path = "/app/data/index-egalite-fh-utf8.csv"
    try:
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            # Normaliser les noms de colonnes
            fieldnames = [normalize_column_name(field) for field in reader.fieldnames]
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            for row in reader:
                data.append(row)
        print(f"Loaded {len(data)} entries from CSV.")  # Log pour vérifier le chargement des données
    except Exception as e:
        print(f"Error loading data: {e}")
    return data

@app.route("/api/v1/entreprises/<siren>", methods=["GET"])
def get_entreprise_by_siren(siren):
    data = load_data()
    entreprise = next((e for e in data if e['Tranche_d_eff_SIREN'] == siren), None)
    if entreprise:
        print(f"Found enterprise: {entreprise}")  # Log pour vérifier l'entreprise trouvée
        return jsonify(entreprise)
    else:
        print(f"No enterprise found with SIREN: {siren}")  # Log pour vérifier si aucune entreprise n'est trouvée
        return jsonify({"message": "Entreprise non trouvée"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
