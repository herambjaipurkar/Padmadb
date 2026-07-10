from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from padmadb.engine import PadmaDB

app = FastAPI(title="PadmaDB Vector Engine", version="1.0.0")

# Initialize database globally (e.g., dimension 384 for standard small embeddings like all-MiniLM-L6-v2)
db = PadmaDB(dimension=384)

class InsertRequest(BaseModel):
    id: str
    vector: List[float]
    metadata: Optional[Dict[str, Any]] = None

class SearchRequest(BaseModel):
    vector: List[float]
    top_k: int = 5

@app.post("/insert")
def insert_vector(req: InsertRequest):
    try:
        db.insert(req.id, req.vector, req.metadata)
        return {"status": "success", "message": f"Vector {req.id} inserted."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/search")
def search_vectors(req: SearchRequest):
    try:
        results = db.search(req.vector, req.top_k)
        return {"status": "success", "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def run_server(host="0.0.0.0", port=8000):
    import uvicorn
    uvicorn.run(app, host=host, port=port)