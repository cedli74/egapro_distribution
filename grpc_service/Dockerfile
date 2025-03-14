FROM python:3.9
WORKDIR /app

# Copier les fichiers nécessaires
COPY service.py requirements.txt /app/
COPY proto/ /app/proto/  # ✅ Copie le dossier proto/

RUN pip install -r requirements.txt

# 📌 Vérifier si le fichier proto existe avant de compiler
RUN ls -l /app/proto/ && \
    python -m grpc_tools.protoc -I/app/proto --python_out=. --grpc_python_out=. /app/proto/egapro.proto

CMD ["python", "service.py"]
