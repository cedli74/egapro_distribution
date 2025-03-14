FROM python:3.9
WORKDIR /app
COPY service.py requirements.txt proto/egapro.proto /app/
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -Iproto --python_out=. --grpc_python_out=. proto/egapro.proto
CMD ["python", "service.py"]
