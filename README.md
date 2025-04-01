README – Lancement et Test du Projet EgaPro Distribution
Ce projet propose une API REST (avec documentation Swagger) et un service gRPC pour interroger des données d’entreprises issues d’un fichier CSV. Le projet utilise Docker et Docker Compose pour déployer les services.

Lancement du Projet
Cloner le dépôt :
Cloner le dépôt depuis GitHub et se placer à la racine du projet.

Vérifier le fichier docker-compose.yml :
Le fichier compose définit quatre services :

rest_api : Exposé sur le port 5000.

grpc_service : Exposé sur le port 50051.

swagger : Exposé sur le port 5001.

nginx : Configuré pour servir de reverse proxy sur le port 80 (configuration du reverse proxy en cours de finalisation).

Lancer l’ensemble des services :
Depuis la racine du projet, exécuter la commande « docker-compose up --build ». Cette commande construit les images, monte les volumes (par exemple, le dossier data contenant le fichier CSV) et démarre tous les conteneurs.

Tester l’API REST
Pour tester l’API REST, accédez via votre navigateur ou un outil comme Postman à une URL de la forme :

  http://localhost:5000/api/v1/entreprises/{SIREN}

où {SIREN} est remplacé par le numéro de SIREN de l’entreprise. Par exemple, pour tester une entreprise avec le SIREN « 352383715 », utilisez :

  http://localhost:5000/api/v1/entreprises/352383715

L’API renvoie les informations complètes de l’entreprise correspondante.

Tester l’Interface Swagger
L’interface Swagger permet de documenter et tester l’API REST.
Pour y accéder, ouvrez votre navigateur à l’adresse :

  http://localhost:5001/apidocs/

Cela vous permettra d’exécuter les endpoints et de voir la documentation.

Tester le Service gRPC
Un client gRPC interactif est inclus dans le projet.
Pour le lancer, ouvrez un terminal et exécutez :

  docker-compose exec grpc_service python client.py

Le client vous demandera d’entrer un numéro de SIREN. Après saisie, il affichera toutes les informations de l’entreprise correspondante, extraites du fichier CSV.

Reverse Proxy Nginx
Nous avons tenté de configurer un reverse proxy Nginx pour centraliser l’accès aux services sous le même domaine et port (80).
L’objectif était de rediriger, par exemple, http://localhost/swagger/ vers http://localhost:5001/apidocs/ et ses ressources associées. Toutefois, la configuration n’a pas pu être finalisée dans son intégralité.
Pour l’instant, l’interface Swagger reste accessible directement via http://localhost:5001/apidocs/ et le reverse proxy partiel (http://localhost/swagger/) est en cours d’amélioration.

Lancement et Test – Résumé
Lancement des services :
Exécutez « docker-compose up --build » depuis la racine du projet.

API REST :
Testez via http://localhost:5000/api/v1/entreprises/{SIREN}

Interface Swagger :
Testez via http://localhost:5001/apidocs/

Service gRPC :
Exécutez « docker-compose exec grpc_service python client.py » et suivez les instructions.

Pour toute question ou suggestion, n’hésitez pas à ouvrir une issue dans le dépôt GitHub.



![image](https://github.com/user-attachments/assets/0ad930eb-f88e-40b3-a98d-ee0e2e771b28)

![image](https://github.com/user-attachments/assets/603dbc09-6b7b-4c97-b51e-6780d5ebabb7)

![image](https://github.com/user-attachments/assets/5c73a670-8146-4903-8935-df60da4d4643)

![image](https://github.com/user-attachments/assets/7a53501f-0e81-4d0f-ba88-aaf9e7435eb1)
