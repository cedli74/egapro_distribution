import csv
import os

def test_csv():
    # Construit le chemin vers le fichier CSV
    csv_path = os.path.join(os.path.dirname(__file__), "data/index-egalite-fh-utf8.csv")
    try:
        with open(csv_path, newline='', encoding='utf-8-sig') as csvfile:
            # Spécifie le séparateur si votre CSV utilise des points-virgules
            reader = csv.DictReader(csvfile, delimiter=';')
            print("📄 Les trois premières lignes du CSV :")
            for i, row in enumerate(reader):
                if i < 3:
                    print(f"Ligne {i+1} : {row}")
                else:
                    break
    except Exception as e:
        print(f"❌ Erreur lors de la lecture du CSV : {e}")

if __name__ == '__main__':
    test_csv()
