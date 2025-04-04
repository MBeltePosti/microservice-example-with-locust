# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["locust", "-f", "tests/performance/locust/run_all.py", "--host", "http://microservice:4999", "--headless", "-u", "5", "-r", "1", "--run-time", "1m"]