FROM python:3.10

WORKDIR /app

COPY requirements.txt ./
COPY proto /app/proto
COPY service.py client.py ./

RUN pip install --no-cache-dir -r requirements.txt

# Génération des fichiers gRPC dans le dossier proto
RUN python -m grpc_tools.protoc -Iproto --python_out=proto --grpc_python_out=proto proto/egapro.proto

ENV PYTHONPATH=/app/proto:$PYTHONPATH

EXPOSE 50051

CMD ["python", "service.py"]
