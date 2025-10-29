from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(query: Query):
    # Temporary mock answer
    return {
        "answer_mode": "sql",
        "sql": "SELECT * FROM inventory WHERE item_id = 'ABC123';",
        "rows": [
            {"item_id": "ABC123", "available_qty": 42, "location": "Warehouse A"}
        ]
    }

@app.get("/healthz")
def health():
    return {"ok": True}
Initial commit: FastAPI backend starter
