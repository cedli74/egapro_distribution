import grpc
from concurrent import futures
import egapro_pb2
import egapro_pb2_grpc
import csv

class EgaproService(egapro_pb2_grpc.EgaproServiceServicer):
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        data = []
        csv_path = "/app/data/index-egalite-fh-utf8.csv"
        try:
            with open(csv_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                data = [row for row in reader]
        except Exception as e:
            print(f"❌ Erreur de chargement CSV: {e}")
        return data

    def GetEntreprises(self, request, context):
        entreprises = [egapro_pb2.Entreprise(**e) for e in self.data]
        return egapro_pb2.EntreprisesResponse(entreprises=entreprises)

    def GetEntrepriseBySiren(self, request, context):
        siren = request.siren
        entreprise = next((e for e in self.data if e['siren'] == siren), None)
        if entreprise:
            return egapro_pb2.EntrepriseResponse(**entreprise)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Entreprise non trouvée')
            return egapro_pb2.EntrepriseResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    egapro_pb2_grpc.add_EgaproServiceServicer_to_server(EgaproService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("✅ gRPC Server lancé sur le port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
