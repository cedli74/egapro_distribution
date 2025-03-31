FROM python:3.10

WORKDIR /app

COPY requirements.txt ./
COPY proto /app/proto
COPY service.py client.py ./

RUN pip install --no-cache-dir -r requirements.txt

# Génération des fichiers gRPC dans le dossier proto
RUN python -m grpc_tools.protoc -Iproto --python_out=proto --grpc_python_out=proto proto/egapro.proto

# Patch du fichier généré pour utiliser un import relatif
# Remplace la ligne qui commence par "import egapro_pb2 as" par "from . import egapro_pb2 as"
RUN sed -i "s/^import egapro_pb2 as/from . import egapro_pb2 as/" proto/egapro_pb2_grpc.py

# Ajout du dossier proto au PYTHONPATH pour être sûr que Python y accède
ENV PYTHONPATH=/app/proto:$PYTHONPATH

EXPOSE 50051

CMD ["python", "service.py"]
