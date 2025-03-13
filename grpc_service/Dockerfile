FROM python:3.9
WORKDIR /app
COPY service.py requirements.txt /app/
COPY proto /app/proto
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/egapro.proto
CMD ["python", "service.py"]
