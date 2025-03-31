FROM python:3.10

WORKDIR /app

COPY requirements.txt ./
COPY proto /app/proto
COPY service.py client.py ./

RUN pip install --no-cache-dir -r requirements.txt

# Supprimez ou commentez la ligne suivante, car le dossier data est monté via volume
# COPY data /app/data

# Régénération des stubs gRPC
RUN rm -f proto/egapro_pb2.py proto/egapro_pb2_grpc.py || true && \
    python -m grpc_tools.protoc -Iproto --python_out=proto --grpc_python_out=proto proto/egapro.proto

RUN touch proto/__init__.py

EXPOSE 50051

CMD ["python", "service.py"]
