from flask import Flask, jsonify
import csv
import re

app = Flask(__name__)

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

def normalize_column_name(name):
    # Remplace les caractères spéciaux et les espaces par des underscores
    return re.sub(r'[^\w\s]', '', name).replace(' ', '_')

@app.route("/api/v1/entreprises/<siren>", methods=["GET"])
def get_entreprise_by_siren(siren):
    data = load_data()
    entreprise = next((e for e in data if e['SIREN'] == siren), None)
    if entreprise:
        print(f"Found enterprise: {entreprise}")  # Log pour vérifier l'entreprise trouvée
        return jsonify(entreprise)
    else:
        print(f"No enterprise found with SIREN: {siren}")  # Log pour vérifier si aucune entreprise n'est trouvée
        return jsonify({"message": "Entreprise non trouvée"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
