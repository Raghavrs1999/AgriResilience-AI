# AgriResilience AI — Production Dockerfile for Google Cloud Run
# Optimized for Google Cloud AI Builder Cup 2026

FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PORT=8080

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code and dataset fixtures
COPY backend/app/ ./backend/app/
COPY backend/data/ ./backend/data/

# Copy frontend static web cockpit
COPY frontend/ ./frontend/

# Expose port for Cloud Run
EXPOSE 8080

# Launch FastAPI ASGI server
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8080"]
