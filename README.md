# dt-avatar-server

A lightweight avatar serving microservice for the Datenshi osu! private server. Serves user profile pictures by user ID, falling back to a default image when none exists.

## Requirements

- Python 3.13+
- Docker (recommended)

## Quick Start

### Docker (recommended)

```bash
docker compose up -d --build
```

### Manual

```bash
pip install -r requirements.txt
gunicorn avatar-server:app --bind 0.0.0.0:5020 --workers 2 --threads 4
```

## API

| Endpoint | Description |
|---|---|
| `GET /<uid>` | Returns avatar for user ID. Falls back to default if not found. |
| `GET /status` | Health check. Returns `{"response": 200, "status": 1}` |

## Avatars

Place PNG files in the `avatars/` directory named by user ID:

```
avatars/
├── -1.png    # default avatar (required)
├── 1000.png
├── 1001.png
└── ...
```

Default port: `5020`
