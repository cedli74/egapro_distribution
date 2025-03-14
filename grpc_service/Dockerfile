# Utilise une image Python
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY service.py requirements.txt /app/

# Copier le dossier proto
COPY proto /app/proto/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Générer les fichiers gRPC à partir du .proto
RUN python -m grpc_tools.protoc -Iproto --python_out=. --grpc_python_out=. proto/egapro.proto

# Exécuter le serveur gRPC
CMD ["python", "service.py"]
