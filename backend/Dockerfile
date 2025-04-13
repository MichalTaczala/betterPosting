
FROM python:3.13-slim


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8080
ENV ENV=prod
ARG ENV_FILE
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip -r requirements.txt

# Copy the rest of the application code into the container
COPY . .
COPY ${ENV_FILE} .env

EXPOSE 8080


CMD ["sh", "-c", "gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8080 --workers 2"]


