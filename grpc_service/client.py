import csv
import os

def load_csv():
    # Construit le chemin vers le fichier CSV situé dans le dossier "data"
    csv_path = os.path.join(os.path.dirname(__file__), "data/index-egalite-fh-utf8.csv")
    try:
        with open(csv_path, newline='', encoding='utf-8-sig') as csvfile:
            # On précise le délimiteur ";" pour découper correctement les colonnes
            reader = csv.DictReader(csvfile, delimiter=';')
            data = list(reader)
        return data
    except Exception as e:
        print(f"Erreur lors du chargement du CSV: {e}")
        return []

def main():
    # Charger le CSV et afficher les trois premières lignes
    data = load_csv()
    if not data:
        print("Aucune donnée chargée.")
        return

    print("📄 Les trois premières lignes du CSV :")
    for i, row in enumerate(data[:3]):
        print(f"Ligne {i+1} : {row}")

    # Demander à l'utilisateur d'entrer un SIREN
    siren_input = input("Entrez le SIREN de l'entreprise recherchée : ").strip()
    
    # Recherche de l'entreprise correspondant au SIREN fourni (on compare en supprimant les espaces)
    entreprise = next((row for row in data if row.get("SIREN", "").strip() == siren_input), None)
    
    if entreprise:
        print("✅ Entreprise trouvée:")
        # Afficher toutes les informations de l'entreprise
        for key, value in entreprise.items():
            print(f"  {key}: {value}")
    else:
        print("❌ Entreprise non trouvée.")

if __name__ == '__main__':
    main()
