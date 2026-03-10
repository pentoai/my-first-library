# Backend

FastAPI + SQLAlchemy + SQLite

## Setup

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

- API: http://localhost:8000
- Docs: http://localhost:8000/docs

## Sample Data

JSON files with sample data are in `data/`.
