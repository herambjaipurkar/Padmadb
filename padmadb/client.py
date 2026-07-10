import requests
from typing import List, Dict, Any

class PadmaClient:
    def __init__(self, host: str = "http://localhost:8000"):
        self.host = host

    def insert(self, vec_id: str, vector: List[float], metadata: Dict[str, Any] = None):
        url = f"{self.host}/insert"
        payload = {"id": vec_id, "vector": vector, "metadata": metadata}
        res = requests.post(url, json=payload)
        return res.json()

    def search(self, vector: List[float], top_k: int = 5):
        url = f"{self.host}/search"
        payload = {"vector": vector, "top_k": top_k}
        res = requests.post(url, json=payload)
        return res.json()