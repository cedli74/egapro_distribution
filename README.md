Lancement et Test du Projet EgaPro Distribution


Ce projet propose une API REST (avec documentation Swagger) et un service gRPC pour interroger des données d’entreprises issues d’un fichier CSV. Le projet utilise Docker et Docker Compose pour déployer les services.

Lancement du Projet avec Docker
Cloner le dépôt :
Clonez le dépôt depuis GitHub et placez-vous à la racine du projet.

Ajouter le fichier CSV complet :
Vous devez placer le fichier CSV complet dans le dossier data situé à la racine du projet. Ce dossier doit contenir votre fichier, par exemple :
data/index-egalite-fh-utf8.csv
Assurez-vous que le fichier CSV est complet et correctement formaté pour que les services puissent le lire.

Vérifier le fichier docker-compose.yml :
Le fichier Compose définit quatre services :

rest_api : Accessible sur le port 5000.

grpc_service : Accessible sur le port 50051.

swagger : Accessible sur le port 5001.

nginx : Configuré pour servir de reverse proxy sur le port 80 (la configuration Nginx pour Swagger n'est pas entièrement finalisée).

Lancer l’ensemble des services :
Depuis la racine du projet, exécutez :

bash
Copier
docker-compose up --build
Cette commande construit les images, monte les volumes (par exemple, le dossier data contenant le CSV) et démarre tous les conteneurs.

Tester l’API REST
Pour tester l’API REST, ouvrez votre navigateur ou utilisez un outil comme Postman et accédez à une URL de la forme :

bash
Copier
http://localhost:5000/api/v1/entreprises/{SIREN}
Par exemple, pour interroger l’entreprise dont le SIREN est 352383715, tapez :

bash
Copier
http://localhost:5000/api/v1/entreprises/352383715
L’API renverra toutes les informations de l’entreprise correspondante.

Tester l’Interface Swagger
L’interface Swagger permet de documenter et de tester l’API REST. Elle est accessible via :

bash
Copier
http://localhost:5001/apidocs/
Vous pouvez utiliser cette interface pour envoyer des requêtes aux endpoints de l’API REST et consulter la documentation.

Tester le Service gRPC
Pour tester le service gRPC, un client gRPC interactif est inclus dans le projet.
Pour le lancer, ouvrez un terminal et exécutez :

bash
Copier
docker-compose exec grpc_service python client.py
Le client vous demandera de saisir un numéro de SIREN et affichera ensuite toutes les informations de l’entreprise correspondante extraites du fichier CSV.

Reverse Proxy Nginx
Nous avons tenté de configurer un reverse proxy Nginx pour centraliser l'accès aux services via le port 80. L’objectif était de rediriger par exemple :

http://localhost/swagger/ vers http://localhost:5001/apidocs/ (et tous les chemins associés).

Cependant, la configuration Nginx pour cette redirection n'est pas entièrement finalisée. Pour l'instant, l’interface Swagger reste accessible directement via http://localhost:5001/apidocs/.

Conclusion
Ce projet vous permet de :

Tester l’API REST en accédant à l’URL :
http://localhost:5000/api/v1/entreprises/{SIREN}
(remplacez {SIREN} par le numéro de SIREN de l’entreprise désirée)

Consulter l’interface Swagger via http://localhost:5001/apidocs/.

Interroger le service gRPC avec le client inclus en lançant :

bash
Copier
docker-compose exec grpc_service python client.py
Important : Assurez-vous que le fichier CSV complet se trouve dans le dossier data à la racine du projet, car il est indispensable pour charger les données d'entreprises.

Pour toute question ou amélioration, n’hésitez pas à ouvrir une issue dans le dépôt.





![image](https://github.com/user-attachments/assets/0ad930eb-f88e-40b3-a98d-ee0e2e771b28)

![image](https://github.com/user-attachments/assets/603dbc09-6b7b-4c97-b51e-6780d5ebabb7)

![image](https://github.com/user-attachments/assets/5c73a670-8146-4903-8935-df60da4d4643)

![image](https://github.com/user-attachments/assets/22afb652-2e46-41ba-94d0-876583e94ea1)


![image](https://github.com/user-attachments/assets/7a53501f-0e81-4d0f-ba88-aaf9e7435eb1)

![image](https://github.com/user-attachments/assets/eb70d90e-fafa-4e54-bc75-3800d5e71ac2)

