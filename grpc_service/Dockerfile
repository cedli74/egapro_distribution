FROM python:3.10

WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt ./
COPY proto /app/proto
COPY service.py client.py ./

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Supprimer d'éventuels anciens stubs et régénérer les fichiers gRPC
RUN rm -f proto/egapro_pb2.py proto/egapro_pb2_grpc.py || true && \
    python -m grpc_tools.protoc -Iproto --python_out=proto --grpc_python_out=proto proto/egapro.proto

# Patch pour que le fichier egapro_pb2_grpc.py utilise un import relatif
RUN sed -i "s/^import egapro_pb2 as/from . import egapro_pb2 as/" proto/egapro_pb2_grpc.py

# S'assurer que le dossier proto est reconnu comme un package Python
RUN touch proto/__init__.py

EXPOSE 50051

CMD ["python", "service.py"]
