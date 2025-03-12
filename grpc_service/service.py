import grpc
from concurrent import futures
import egapro_pb2
import egapro_pb2_grpc
import csv
import os

def generate_proto():
    import subprocess
    subprocess.run(["python", "-m", "grpc_tools.protoc", "-I./proto", "--python_out=.", "--grpc_python_out=.", "./proto/egapro.proto"], check=True)

generate_proto()

class EgaProService(egapro_pb2_grpc.EgaProServiceServicer):
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        data = []
        csv_path = os.path.join(os.path.dirname(__file__), "../data/index-egalite-fh-utf8.csv")
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(egapro_pb2.Entreprise(siren=row['siren'], name=row['name']))
        return data

    def GetEntreprises(self, request, context):
        return egapro_pb2.EntrepriseList(entreprises=self.data)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
egapro_pb2_grpc.add_EgaProServiceServicer_to_server(EgaProService(), server)
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()
