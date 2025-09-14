# URL Shortener

A simple FastAPI service that shortens URLs and stores them in SQLite.

## Quick Start

```bash
# Install dependencies
uv sync

# Set up environment
echo "DATABASE_NAME=urls.db" > .env

# Run server
uvicorn src.main:app --reload
```

## Usage

Send a POST request to `/api/shorten_url` with your URL:

```bash
curl -X POST "http://localhost:8000/api/shorten_url" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "input_url=https://example.com/very/long/url"
```

Returns: `https://maxshorten.er/abc123`

## How It Works

1. Takes your long URL
2. Generates a 6-character hash using SHA256
3. Stores the mapping in SQLite
4. Returns the shortened URL

## Tech Stack

- **FastAPI** - Web framework
- **SQLite** - Database
- **Pydantic** - Settings management
- **SHA256** - URL hashing
