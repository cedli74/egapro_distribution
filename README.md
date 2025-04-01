README – Lancement et Test du Projet EgaPro Distribution
Ce projet propose une API REST (avec documentation Swagger) et un service gRPC pour interroger des données d’entreprises issues d’un fichier CSV. Nous utilisons Docker et Docker Compose pour faciliter le déploiement des différents services.

Prérequis
Docker : Installer Docker

Docker Compose : Installer Docker Compose

Lancement du Projet avec Docker
Cloner le dépôt :

Ouvrez votre terminal et clonez le dépôt :

bash
Copier
git clone https://github.com/votre-utilisateur/egapro_distribution.git
cd egapro_distribution
Vérifier le fichier docker-compose.yml :

Le fichier docker-compose.yml se trouve à la racine du projet et définit plusieurs services :

rest_api : Le service de l'API REST, accessible sur le port 5000.

grpc_service : Le service gRPC, accessible sur le port 50051.

swagger : L'interface Swagger, accessible sur le port 5001.

nginx : Un reverse proxy (en cours de configuration) accessible sur le port 80.

Exemple de configuration (extrait) :

yaml
Copier
version: '3'

services:
  rest_api:
    build: ./rest_api
    ports:
      - "5000:5000"
    volumes:
      - ./data:/app/data
    restart: always

  grpc_service:
    build: ./grpc_service
    ports:
      - "50051:50051"
    volumes:
      - ./data:/app/data
    restart: always

  swagger:
    build: ./swagger
    ports:
      - "5001:5001"
    restart: always

  nginx:
    build: ./nginx
    ports:
      - "80:80"
    depends_on:
      - rest_api
      - grpc_service
      - swagger
    restart: always
Lancer tous les services :

Dans la racine du projet, lancez la commande suivante pour construire les images et démarrer les conteneurs :

bash
Copier
docker-compose up --build
Cette commande effectue les opérations suivantes :

Build : Docker Compose construit les images pour chaque service en se basant sur les Dockerfiles présents dans les dossiers respectifs (rest_api, grpc_service, swagger, nginx).

Montage des volumes : Par exemple, le dossier data (contenant votre fichier CSV) est monté dans les conteneurs rest_api et grpc_service.

Démarrage des conteneurs : Une fois les images construites, les conteneurs sont démarrés et les ports sont mappés pour rendre les services accessibles depuis votre machine.

Vous verrez dans le terminal les logs des différents services. Une fois les conteneurs démarrés, vous pouvez laisser ce terminal ouvert ou l'exécuter en mode détaché avec l'option -d.

Tester l'API REST
Pour tester l'API REST, ouvrez votre navigateur et accédez à une URL construite de la manière suivante :

bash
Copier
http://localhost:5000/api/v1/entreprises/352383715
Dans cet exemple, 352383715 représente le numéro de SIREN d'une entreprise. L'API REST renverra les informations associées à cette entreprise.

Tester l'Interface Swagger
L'interface Swagger est destinée à documenter et permettre de tester l'API REST. Elle est accessible directement via :

bash
Copier
http://localhost:5001/apidocs/
Vous pouvez l'utiliser pour envoyer des requêtes à l'API REST et voir la documentation de tous les endpoints.

Tester le Service gRPC
Pour tester le service gRPC, un client est inclus dans le projet. Pour lancer ce client :

Ouvrez un nouveau terminal.

Exécutez la commande suivante :

bash
Copier
docker-compose exec grpc_service python client.py
Le client vous demandera d'entrer un numéro de SIREN. Saisissez par exemple un SIREN existant (tel que présent dans votre CSV), et le client affichera toutes les informations de l'entreprise correspondante.

Reverse Proxy Nginx (En Cours de Finalisation)
Nous avons entrepris de configurer un reverse proxy avec Nginx afin d'unifier l'accès aux services via le port 80. L'objectif est de rediriger par exemple :

http://localhost/swagger/ vers http://localhost:5001/apidocs/ (avec redirection des ressources statiques).

Cependant, cette configuration n'est pas encore finalisée. Pour l'instant, l'interface Swagger est accessible directement via http://localhost:5001/apidocs/. Nous avons tenté de configurer Nginx pour rediriger http://localhost/swagger/, mais le développement n'est pas terminé. Vous pouvez continuer à tester Swagger via son URL directe.

Conclusion
Ce projet vous permet de tester :

Une API REST accessible via http://localhost:5000/api/v1/entreprises/{SIREN} (ajoutez le numéro de SIREN à la fin de l'URL),

Une interface Swagger pour la documentation et les tests de l'API REST,

Un service gRPC pour interroger les données d’entreprises via un client interactif.

Pour l'instant, nous n'avons pas finalisé la configuration du reverse proxy Nginx pour Swagger, et il faut continuer à accéder à Swagger via http://localhost:5001/apidocs/.

N'hésitez pas à consulter les logs de Docker pour suivre le démarrage des conteneurs et poser vos questions via le système d'issues du dépôt si vous rencontrez des difficultés.
