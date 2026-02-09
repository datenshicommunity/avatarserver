# Stage 1: Build dependencies
FROM python:3.13-alpine AS builder

WORKDIR /build

RUN apk add --no-cache gcc musl-dev

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Runtime
FROM python:3.13-alpine

WORKDIR /app

COPY --from=builder /install /usr/local

COPY avatar-server.py .
COPY avatars/-1.png avatars/-1.png

EXPOSE 5020

CMD ["gunicorn", "avatar-server:app", \
     "--bind", "0.0.0.0:5020", \
     "--workers", "2", \
     "--threads", "4", \
     "--access-logfile", "-"]
