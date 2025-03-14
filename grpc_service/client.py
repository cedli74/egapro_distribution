import grpc
import egapro_pb2
import egapro_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = egapro_pb2_grpc.EgaproServiceStub(channel)
        
        print("🔍 Demande de toutes les entreprises...")
        response = stub.GetEntreprises(egapro_pb2.EntreprisesRequest())
        for entreprise in response.entreprises:
            print(f"🏢 {entreprise.siren} - {entreprise.nom} - Score: {entreprise.score_egalite}")
        
        print("\n🔍 Recherche d'une entreprise par SIREN...")
        siren = "123456789"  # Remplace par un SIREN valide
        try:
            response = stub.GetEntrepriseBySiren(egapro_pb2.EntrepriseRequest(siren=siren))
            print(f"✅ Trouvé : {response.nom} - {response.score_egalite} - {response.adresse}")
        except grpc.RpcError as e:
            print(f"❌ Erreur : {e.code()} - {e.details()}")

if __name__ == "__main__":
    run()
