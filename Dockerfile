FROM python:3.8-slim-buster

WORKDIR /app

COPY server.py .

CMD ["python3", "server.py"]