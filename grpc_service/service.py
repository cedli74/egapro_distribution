import grpc
from concurrent import futures
import csv
import sys

import egapro_pb2
import egapro_pb2_grpc

# Ajouter le dossier courant dans le PATH
sys.path.append(".")

class EgaproService(egapro_pb2_grpc.EgaproServiceServicer):
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        data = []
        csv_path = "data/index-egalite-fh-utf8.csv"  # Mets le bon chemin ici
        try:
            with open(csv_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    data.append(row)
        except Exception as e:
            print(f"Erreur chargement CSV: {e}")
        return data

    def GetEntreprises(self, request, context):
        entreprises = [
            egapro_pb2.Entreprise(
                siren=e["siren"],
                nom=e["nom"],
                score_egalite=int(e["score_egalite"]),
                adresse=e["adresse"]
            ) for e in self.data
        ]
        return egapro_pb2.EntreprisesResponse(entreprises=entreprises)

    def GetEntrepriseBySiren(self, request, context):
        siren = request.siren
        entreprise = next((e for e in self.data if e["siren"] == siren), None)

        if entreprise:
            return egapro_pb2.EntrepriseResponse(
                siren=entreprise["siren"],
                nom=entreprise["nom"],
                score_egalite=int(entreprise["score_egalite"]),
                adresse=entreprise["adresse"]
            )
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Entreprise non trouvée")
            return egapro_pb2.EntrepriseResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    egapro_pb2_grpc.add_EgaproServiceServicer_to_server(EgaproService(), server)
    server.add_insecure_port("[::]:50051")
    print("✅ Serveur gRPC en écoute sur le port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
