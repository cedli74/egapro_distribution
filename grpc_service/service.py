import grpc
from concurrent import futures
import os, csv
import proto.egapro_pb2 as egapro_pb2
import proto.egapro_pb2_grpc as egapro_pb2_grpc

def load_csv():
    # Construit le chemin vers le fichier CSV dans le dossier data (dans grpc_service/data)
    csv_path = os.path.join(os.path.dirname(__file__), "data/index-egalite-fh-utf8.csv")
    data = []
    try:
        with open(csv_path, newline='', encoding='utf-8-sig') as csvfile:
            # Utiliser le point-virgule comme séparateur
            reader = csv.DictReader(csvfile, delimiter=';')
            data = list(reader)
        if data:
            print(f"✅ {len(data)} entreprises chargées depuis le CSV.")
            print("📄 Extrait des 3 premières lignes du CSV :")
            for i, row in enumerate(data[:3]):
                print(f"  Ligne {i+1} : {row}")
        else:
            print("❌ Aucun enregistrement chargé depuis le CSV.")
    except Exception as e:
        print(f"❌ Erreur lors du chargement du CSV : {e}")
    return data

class EgaproService(egapro_pb2_grpc.EgaproServiceServicer):
    def __init__(self):
        self.data = load_csv()

    def GetEntreprises(self, request, context):
        entreprises = []
        # Pour chaque ligne du CSV, on tente de créer un message Entreprise.
        # On s'attend à ce que les clés du dictionnaire correspondent exactement aux noms de champs définis dans votre message proto.
        for row in self.data:
            try:
                entreprises.append(egapro_pb2.Entreprise(**row))
            except Exception as ex:
                print(f"Erreur lors de la création d'une entreprise: {ex}")
        return egapro_pb2.EntreprisesResponse(entreprises=entreprises)

    def GetEntrepriseBySiren(self, request, context):
        siren_input = request.siren.strip()
        # Recherche de l'entreprise dans le CSV en comparant le champ 'SIREN'
        entreprise = next((row for row in self.data if row.get("SIREN", "").strip() == siren_input), None)
        if entreprise:
            try:
                return egapro_pb2.EntrepriseResponse(entreprise=egapro_pb2.Entreprise(**entreprise))
            except Exception as ex:
                context.set_details(f"Erreur lors de la création de l'entreprise: {ex}")
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
