FROM python:3.9
WORKDIR /app

# Copier les fichiers Python
COPY service.py requirements.txt /app/

# Copier le dossier proto
COPY grpc_service/proto /app/proto  # ✅ Correction du chemin

RUN pip install -r requirements.txt

# Compiler les fichiers gRPC
RUN ls -l /app/proto && \
    python -m grpc_tools.protoc -I/app/proto --python_out=. --grpc_python_out=. /app/proto/egapro.proto

CMD ["python", "service.py"]
