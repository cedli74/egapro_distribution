import grpc
import proto.egapro_pb2 as egapro_pb2
import proto.egapro_pb2_grpc as egapro_pb2_grpc

def run():
    # Se connecter au serveur gRPC
    channel = grpc.insecure_channel('localhost:50051')
    stub = egapro_pb2_grpc.EgaproServiceStub(channel)

    # 🔹 Tester la récupération de toutes les entreprises
    response = stub.GetEntreprises(egapro_pb2.EntreprisesRequest())
    print("✅ Entreprises reçues:", response)

    # 🔹 Tester la récupération d'une entreprise par SIREN
    siren_test = "123456789"  # Remplace avec un vrai SIREN
    response = stub.GetEntrepriseBySiren(egapro_pb2.EntrepriseRequest(siren=siren_test))
    print("✅ Entreprise trouvée:", response)

if __name__ == "__main__":
    run()
