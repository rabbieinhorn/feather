import os
from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel

# Simple API key guard (set API_KEY in Render env vars)
API_KEY = os.getenv("API_KEY", "dev-key")

def require_key(x_api_key: str | None = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

app = FastAPI()

class Query(BaseModel):
    question: str

@app.get("/")
def root():
    return {"status": "ok", "message": "ERP Chatbot backend alive. Try GET /healthz or POST /ask."}

@app.get("/healthz")
def health():
    return {"ok": True}

@app.post("/ask")
def ask(query: Query, _=Depends(require_key)):
    # Temporary mock answer
    return {
        "answer_mode": "sql",
        "sql": "SELECT * FROM inventory WHERE item_id = 'ABC123';",
        "rows": [
            {"item_id": "ABC123", "available_qty": 42, "location": "Warehouse A"}
        ]
    }
