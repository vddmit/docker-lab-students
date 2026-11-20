
FROM python:3.12-slim AS builder

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build

COPY requirements.txt .

RUN pip wheel --no-cache-dir --wheel-dir=/wheels -r requirements.txt


FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends libpq5 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /wheels /wheels

RUN pip install --no-cache-dir --no-index /wheels/* \
    && rm -rf /wheels

COPY app/ .

EXPOSE 5001

CMD ["python", "app.py"]
