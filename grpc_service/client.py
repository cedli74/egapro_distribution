import grpc
import random
import proto.egapro_pb2 as egapro_pb2
import proto.egapro_pb2_grpc as egapro_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = egapro_pb2_grpc.EgaproServiceStub(channel)

        # Récupération de toutes les entreprises
        response = stub.GetEntreprises(egapro_pb2.EntreprisesRequest())
        entreprises = response.entreprises

        if not entreprises:
            print("❌ Aucune entreprise trouvée.")
            return

        # Choix aléatoire d'une entreprise parmi la liste récupérée
        enterprise = random.choice(entreprises)
        random_siren = enterprise.siren
        print(f"🔍 SIREN aléatoire choisi: {random_siren}")

        # Recherche de l'entreprise par son SIREN
        response_detail = stub.GetEntrepriseBySiren(egapro_pb2.EntrepriseRequest(siren=random_siren))
        ent = response_detail.entreprise

        if ent and ent.siren:
            print("✅ Détails de l'entreprise :")
            # Affichage de tous les champs disponibles dans le message
            for field in ent.DESCRIPTOR.fields:
                value = getattr(ent, field.name)
                print(f"  {field.name}: {value}")
        else:
            print("❌ Entreprise non trouvée")

if __name__ == "__main__":
    run()
