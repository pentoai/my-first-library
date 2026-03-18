# My First Library 🤓📚

A minimal full-stack scaffold designed for progressive learning.

## Project Structure

```
my-first-library/
├── docker-compose.yml   # Defines the database and backend services
├── backend/          # FastAPI + SQLAlchemy + SQLite
│   ├── Dockerfile    # Builds the backend container
│   ├── main.py       # API endpoints
│   ├── models.py     # SQLAlchemy models
│   ├── schemas.py    # Pydantic schemas
│   ├── database.py   # Database setup
│   ├── data/         # Sample CSV data
│   └── requirements.txt
└── frontend/          # React + TypeScript + Vite
    ├── src/
    │   ├── components/    # React components
    │   ├── services/      # API client
    │   ├── types/         # TypeScript interfaces
    │   └── App.tsx        # Main app
    └── package.json
```

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and Docker Compose
- Python 3.10+ (for running tests locally)
- Node.js 18+ and npm (for the frontend)

## Quick Start

### Start the databases and backend

Docker handles PostgreSQL and the FastAPI server for you:

```bash
docker compose up -d
```

This starts two services (defined in `docker-compose.yml`):

- `db` — PostgreSQL for the app on port 5432
- `backend` — FastAPI app on port 8000

> **Already have PostgreSQL installed locally?** You can skip Docker for the databases and create them manually instead.
> Then update `DATABASE_URL` in your `.env` file to point to your local instance. You can still run just the backend container with `docker compose up -d backend` if you prefer.

The API is now running at http://localhost:8000

- Interactive docs: http://localhost:8000/docs

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

- Frontend: http://localhost:5173

## Sample Data Available

JSON files are provided in `backend/data/:

- `authors.json`: Sample author data with IDs (name, nationality, birth_date)
- `books.json`: Sample book data with IDs (title, author_id, year, genre, available)
