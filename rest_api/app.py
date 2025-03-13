from flask import Flask, jsonify
import csv

app = Flask(__name__)

def load_data():
    data = []
    csv_path = "/app/data/index-egalite-fh-utf8.csv"
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

@app.route("/api/v1/entreprises/<siren>", methods=["GET"])
def get_entreprise_by_siren(siren):
    data = load_data()
    entreprise = next((e for e in data if e['siren'] == siren), None)
    if entreprise:
        return jsonify(entreprise)
    else:
        return jsonify({"message": "Entreprise non trouvée"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
