# Utiliser l'image Python
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
COPY egapro.proto .
COPY service.py .
COPY data/ data/  # S'assurer que les données CSV sont copiées

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Générer les fichiers gRPC à partir du fichier .proto
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. egapro.proto

# Lancer le serveur gRPC
CMD ["python", "service.py"]
