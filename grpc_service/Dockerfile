# Utilisation de Python 3.10
FROM python:3.10

# Définition du dossier de travail
WORKDIR /app

# Copie des fichiers nécessaires
COPY requirements.txt ./
COPY proto /app/proto
COPY service.py client.py ./

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Génération des fichiers gRPC
RUN python -m grpc_tools.protoc -Iproto --python_out=proto --grpc_python_out=proto proto/egapro.proto


# Expose le port gRPC
EXPOSE 50051

# Commande pour démarrer le serveur gRPC
CMD ["python", "service.py"]
