import grpc
from concurrent import futures
import proto.egapro_pb2 as egapro_pb2
import proto.egapro_pb2_grpc as egapro_pb2_grpc
import csv
import os

class EgaproService(egapro_pb2_grpc.EgaproServiceServicer):
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        data = []
        # Construire le chemin vers le fichier CSV en partant du dossier courant (/app)
        csv_path = os.path.join(os.path.dirname(__file__), "data/index-egalite-fh-utf8.csv")
        try:
            with open(csv_path, newline='', encoding='utf-8-sig') as csvfile:
                # Utiliser le point-virgule comme séparateur
                reader = csv.DictReader(csvfile, delimiter=';')
                data = [row for row in reader]
            if data:
                print(f"✅ {len(data)} entreprises chargées depuis le fichier CSV.")
                print(f"🔍 Colonnes disponibles : {list(data[0].keys())}")
                print("📄 Extrait des premières lignes du CSV :")
                for i, example in enumerate(data[:3]):
                    print(f"  Ligne {i+1} : {example}")
            else:
                print("❌ Aucun enregistrement chargé depuis le CSV.")
        except Exception as e:
            print(f"❌ Erreur lors du chargement des données : {e}")
        return data

    def GetEntreprises(self, request, context):
        # Récupérer les noms des champs définis dans le message Entreprise
        allowed_fields = set(egapro_pb2.Entreprise.DESCRIPTOR.fields_by_name.keys())
        entreprises = []
        for row in self.data:
            # Filtrer le dictionnaire pour ne garder que les champs attendus
            filtered = {k: row[k] for k in row if k in allowed_fields}
            try:
                entreprises.append(egapro_pb2.Entreprise(**filtered))
            except Exception as ex:
                print(f"Erreur lors de la création d'une entreprise : {ex}")
        return egapro_pb2.EntreprisesResponse(entreprises=entreprises)

    def GetEntrepriseBySiren(self, request, context):
        siren = request.siren.strip()
        # Rechercher dans les données la ligne dont la colonne 'SIREN' correspond exactement au SIREN fourni
        entreprise = next((row for row in self.data if row.get('SIREN', '').strip() == siren), None)
        if entreprise:
            allowed_fields = set(egapro_pb2.Entreprise.DESCRIPTOR.fields_by_name.keys())
            filtered = {k: entreprise[k] for k in entreprise if k in allowed_fields}
            return egapro_pb2.EntrepriseResponse(entreprise=egapro_pb2.Entreprise(**filtered))
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Entreprise non trouvée")
            return egapro_pb2.EntrepriseResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    egapro_pb2_grpc.add_EgaproServiceServicer_to_server(EgaproService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("✅ Serveur gRPC en cours d'exécution sur le port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
