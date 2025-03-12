from flask import Flask, jsonify
from flasgger import Swagger
import csv
import os
 
app = Flask(__name__)
 
# Charger la documentation depuis swagger.yml
swagger = Swagger(app, template_file=os.path.join(os.path.dirname(__file__), "swagger.yml"))
 
def load_data():
    data = []
    with open("../data/index-egalite-fh-utf8.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append({"siren": row["siren"], "name": row["name"]})
    return data
 
data = load_data()
 
@app.route("/api/v1/entreprises", methods=["GET"])
def get_entreprises():
    return jsonify(data)
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
