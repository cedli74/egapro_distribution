import grpc
from concurrent import futures
import os, csv
import proto.egapro_pb2 as egapro_pb2
import proto.egapro_pb2_grpc as egapro_pb2_grpc

def load_csv():
    # Construit le chemin vers le CSV dans le dossier data
    csv_path = os.path.join(os.path.dirname(__file__), "data/index-egalite-fh-utf8.csv")
    try:
        with open(csv_path, newline='', encoding='utf-8-sig') as csvfile:
            # Utiliser ";" comme séparateur
            reader = csv.DictReader(csvfile, delimiter=';')
            data = list(reader)
        if data:
            print(f"✅ {len(data)} entreprises chargées depuis le CSV.")
            # Afficher un extrait pour vérifier le chargement
            print("📄 Extrait des 3 premières lignes du CSV :")
            for i, row in enumerate(data[:3]):
                print(f"  Ligne {i+1} : {row}")
        else:
            print("❌ Aucun enregistrement chargé depuis le CSV.")
        return data
    except Exception as e:
        print(f"❌ Erreur lors du chargement du CSV: {e}")
        return []

class EgaproService(egapro_pb2_grpc.EgaproServiceServicer):
    def __init__(self):
        self.data = load_csv()

    def GetEntreprises(self, request, context):
        entreprises = []
        for row in self.data:
            try:
                # On suppose que votre message Entreprise a des champs dont les noms correspondent exactement aux en-têtes du CSV
                entreprises.append(egapro_pb2.Entreprise(**row))
            except Exception as e:
                print(f"Erreur lors de la création d'une entreprise: {e}")
        return egapro_pb2.EntreprisesResponse(entreprises=entreprises)

    def GetEntrepriseBySiren(self, request, context):
        siren_input = request.siren.strip()
        entreprise = next((row for row in self.data if row.get("SIREN", "").strip() == siren_input), None)
        if entreprise:
            try:
                return egapro_pb2.EntrepriseResponse(entreprise=egapro_pb2.Entreprise(**entreprise))
            except Exception as e:
                context.set_details(f"Erreur lors de la création de l'entreprise: {e}")
                context.set_code(grpc.StatusCode.INTERNAL)
                return egapro_pb2.EntrepriseResponse()
        else:
            context.set_details("Entreprise non trouvée")
            context.set_code(grpc.StatusCode.NOT_FOUND)
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
