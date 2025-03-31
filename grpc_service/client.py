print("🔍 Récupération de toutes les entreprises...")
         response = stub.GetEntreprises(egapro_pb2.EntreprisesRequest())
         for entreprise in response.entreprises:
             # Utilisation de 'raison_sociale' à la place de 'nom'
             print(f"{entreprise.siren} - {entreprise.raison_sociale} - Score: {entreprise.score_egalite}")
             # Utilisation des champs existants dans votre message proto
             print(f"{entreprise.siren} - {entreprise.raison_sociale} - Score: {entreprise.note_index}")
 
         # Demande à l'utilisateur d'entrer un SIREN
         siren_input = input("\nEntrez le SIREN de l'entreprise recherchée : ").strip()
         print(f"\n🔍 Recherche de l'entreprise avec SIREN {siren_input}...")
         try:
             response = stub.GetEntrepriseBySiren(egapro_pb2.EntrepriseRequest(siren=siren_input))
             # Vérification avec 'raison_sociale' plutôt que 'nom'
             if response.raison_sociale:
                 print(f"✅ Trouvé: {response.raison_sociale} - Score: {response.score_egalite} - Adresse: {response.adresse}")
             entreprise = response.entreprise
             if entreprise.raison_sociale:
                 print(f"✅ Trouvé: {entreprise.raison_sociale} - Score: {entreprise.note_index} - Adresse: {entreprise.adresse}")
             else:
                 print("❌ Erreur: Entreprise non trouvée")
         except grpc.RpcError as e:
