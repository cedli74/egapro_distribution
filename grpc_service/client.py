import grpc
import proto.egapro_pb2 as egapro_pb2
import proto.egapro_pb2_grpc as egapro_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = egapro_pb2_grpc.EgaproServiceStub(channel)

        # Récupération et affichage de toutes les entreprises
        print("🔍 Récupération de toutes les entreprises...")
        response = stub.GetEntreprises(egapro_pb2.EntreprisesRequest())
        for entreprise in response.entreprises:
            # Utilisation de 'raison_sociale' à la place de 'nom'
            print(f"{entreprise.siren} - {entreprise.raison_sociale} - Score: {entreprise.score_egalite}")

        # Demande à l'utilisateur d'entrer un SIREN
        siren_input = input("\nEntrez le SIREN de l'entreprise recherchée : ").strip()
        print(f"\n🔍 Recherche de l'entreprise avec SIREN {siren_input}...")
        try:
            response = stub.GetEntrepriseBySiren(egapro_pb2.EntrepriseRequest(siren=siren_input))
            # Vérification avec 'raison_sociale' plutôt que 'nom'
            if response.raison_sociale:
                print(f"✅ Trouvé: {response.raison_sociale} - Score: {response.score_egalite} - Adresse: {response.adresse}")
            else:
                print("❌ Erreur: Entreprise non trouvée")
        except grpc.RpcError as e:
            print(f"❌ Erreur: {e.details()}")

if __name__ == "__main__":
    run()
