import grpc
from concurrent import futures
import egapro_pb2
import egapro_pb2_grpc
import csv
import os

class EgaProService(egapro_pb2_grpc.EgaProServiceServicer):
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        data = []
        csv_path = "/app/data/index-egalite-fh-utf8.csv"  # Chemin correct pour Docker
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')  # Utilisez le point-virgule comme délimiteur
            print(f"CSV Headers: {reader.fieldnames}")  # Affiche les en-têtes du CSV
            for row in reader:
                if 'SIREN' in row and 'Raison Sociale' in row:  # Utilisez les noms exacts des colonnes
                    data.append(egapro_pb2.Entreprise(siren=row['SIREN'], name=row['Raison Sociale']))
                else:
                    print(f"Missing expected fields in row: {row}")  # Affiche uniquement les lignes problématiques
        return data

    def GetEntreprises(self, request, context):
        return egapro_pb2.EntrepriseList(entreprises=self.data)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
egapro_pb2_grpc.add_EgaProServiceServicer_to_server(EgaProService(), server)
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()
