# My First Library 🤓📚

A minimal full-stack scaffold designed for progressive learning.

## Project Structure

```
my-first-library/
├── backend/          # FastAPI + SQLAlchemy + SQLite
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

## Quick Start

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

- API: http://localhost:8000
- Docs: http://localhost:8000/docs (available once you implement endpoints)

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
