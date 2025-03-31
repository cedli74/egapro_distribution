FROM python:3.10

WORKDIR /app

# Copier les fichiers nécessaires (sauf data, monté en volume)
COPY requirements.txt ./
COPY proto /app/proto
COPY service.py client.py ./

RUN pip install --no-cache-dir -r requirements.txt

# Forcer la régénération des stubs gRPC :
RUN rm -f proto/egapro_pb2.py proto/egapro_pb2_grpc.py || true && \
    python -m grpc_tools.protoc -Iproto --python_out=proto --grpc_python_out=proto proto/egapro.proto && \
    sed -i "s/^import egapro_pb2 as/from . import egapro_pb2 as/" proto/egapro_pb2_grpc.py && \
    touch proto/__init__.py

# Ajout du dossier proto dans le PYTHONPATH pour que l'import fonctionne
ENV PYTHONPATH=/app/proto:$PYTHONPATH

EXPOSE 50051

CMD ["python", "service.py"]
