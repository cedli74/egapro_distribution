FROM python:3.9
WORKDIR /app
COPY service.py requirements.txt /app/
COPY proto /app/proto
RUN pip install -r requirements.txt
CMD ["python", "service.py"]
