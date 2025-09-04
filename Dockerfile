# ---------- Stage 1: Build Recharts component ----------
FROM node:20-alpine AS fe-build
WORKDIR /fe

# install deps
COPY components/recharts/frontend/package.json ./frontend/package.json
WORKDIR /fe/frontend
RUN npm install

# copy rest and build
COPY components/recharts/frontend/ /fe/frontend/
RUN npm run build

# ---------- Stage 2: Python/Streamlit ----------
FROM python:3.11-slim AS app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_HEADLESS=true

WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# app source
COPY app.py ./app.py
COPY components/recharts/__init__.py ./components/recharts/__init__.py

# copy built assets into Python package path
RUN mkdir -p components/recharts/frontend_dist
COPY --from=fe-build /fe/frontend/dist/ components/recharts/frontend_dist/

EXPOSE 8501
HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
  CMD curl -fsS http://localhost:8501/healthz || exit 1

CMD ["streamlit", "run", "app.py"]
