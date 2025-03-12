FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install grpcio grpcio-tools

# Compiler les fichiers proto
RUN python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/egapro.proto

CMD ["python", "service.py"]
