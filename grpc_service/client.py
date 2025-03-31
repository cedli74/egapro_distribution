import grpc
import proto.egapro_pb2 as egapro_pb2
import proto.egapro_pb2_grpc as egapro_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = egapro_pb2_grpc.EgaproServiceStub(channel)

        # Demande à l'utilisateur d'entrer un SIREN
        siren_input = input("Entrez le SIREN de l'entreprise recherchée : ").strip()
        print(f"\n🔍 Recherche de l'entreprise avec SIREN {siren_input}...")
        try:
            response = stub.GetEntrepriseBySiren(egapro_pb2.EntrepriseRequest(siren=siren_input))
            entreprise = response.entreprise
            # Vérifier que le champ 'SIREN' n'est pas vide pour valider que l'entreprise a été trouvée
            if entreprise and entreprise.siren:
                print("✅ Entreprise trouvée:")
                # Itérer sur tous les champs définis dans le message et afficher leur nom et leur valeur
                for field in entreprise.DESCRIPTOR.fields:
                    value = getattr(entreprise, field.name)
                    print(f"  {field.name}: {value}")
            else:
                print("❌ Entreprise non trouvée")
        except grpc.RpcError as e:
            print(f"❌ Erreur: {e.details()}")

if __name__ == "__main__":
    run()
