import grpc
from concurrent import futures
import proto.egapro_pb2 as egapro_pb2
import proto.egapro_pb2_grpc as egapro_pb2_grpc
import csv

class EgaproService(egapro_pb2_grpc.EgaproServiceServicer):
    def __init__(self):
        # On appelle load_data() ici, il doit exister dans la classe
        self.data = self.load_data()

    def load_data(self):
        data = []
        csv_path = "/app/data/index-egalite-fh-utf8.csv"
        # Utilisation du délimiteur approprié, ici le point-virgule, si nécessaire
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                data.append(row)
        return data

    def GetEntreprises(self, request, context):
        entreprises = [egapro_pb2.Entreprise(**e) for e in self.data]
        return egapro_pb2.EntreprisesResponse(entreprises=entreprises)

def GetEntreprises(self, request, context):
    # Récupère l'ensemble des noms de champs définis dans le message Entreprise
    allowed_fields = set(egapro_pb2.Entreprise.DESCRIPTOR.fields_by_name.keys())
    
    entreprises = []
    for e in self.data:
        # Filtrer le dictionnaire pour ne garder que les clés attendues
        filtered = {k: v for k, v in e.items() if k in allowed_fields}
        entreprises.append(egapro_pb2.Entreprise(**filtered))
        
    return egapro_pb2.EntreprisesResponse(entreprises=entreprises)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    egapro_pb2_grpc.add_EgaproServiceServicer_to_server(EgaproService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("✅ Serveur gRPC en cours d'exécution sur le port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
