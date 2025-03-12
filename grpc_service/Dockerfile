FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install grpcio grpcio-tools

# Générer les fichiers gRPC
RUN python -m grpc_tools.protoc -Iproto --python_out=. --grpc_python_out=. proto/egapro.proto

CMD ["python", "service.py"]
