FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install grpcio grpcio-tools

# Vérifier que le dossier 'proto' existe et contient bien le fichier .proto
RUN ls -la /app/proto

# Compiler les fichiers Protobuf
RUN python -m grpc_tools.protoc -I/app/proto --python_out=/app --grpc_python_out=/app /app/proto/egapro.proto

CMD ["python", "service.py"]
