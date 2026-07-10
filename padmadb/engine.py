import numpy as np
import json
import os
from typing import List, Dict, Any, Tuple

class PadmaDB:
    def __init__(self, dimension: int, persist_path: str = "padmadb_storage.json"):
        """Initialize the vector database in memory."""
        self.dimension = dimension
        self.persist_path = persist_path
        self.vectors = []     # List of numpy arrays
        self.metadata = []    # List of dictionaries holding data/IDs
        self.load()

    def insert(self, vec_id: str, vector: List[float], meta: Dict[str, Any] = None):
        """Insert a vector into the database."""
        if len(vector) != self.dimension:
            raise ValueError(f"Vector dimension must be {self.dimension}, got {len(vector)}")
        
        self.vectors.append(np.array(vector, dtype=np.float32))
        meta_record = {"id": vec_id, "meta": meta or {}}
        self.metadata.append(meta_record)
        self.save()

    def search(self, query_vector: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
        """Perform exact nearest neighbor search using Cosine Similarity."""
        if not self.vectors:
            return []
            
        q_vec = np.array(query_vector, dtype=np.float32)
        db_vecs = np.stack(self.vectors)
        
        # Calculate Cosine Similarity: dot(a, b) / (norm(a) * norm(b))
        dot_products = np.dot(db_vecs, q_vec)
        norms = np.linalg.norm(db_vecs, axis=1) * np.linalg.norm(q_vec)
        
        # Avoid division by zero
        similarities = np.divide(dot_products, norms, out=np.zeros_like(dot_products), where=norms!=0)
        
        # Get top K indices sorted descending
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            results.append({
                "id": self.metadata[idx]["id"],
                "score": float(similarities[idx]),
                "metadata": self.metadata[idx]["meta"]
            })
        return results

    def save(self):
        """Persist state to local disk as JSON."""
        data = {
            "dimension": self.dimension,
            "vectors": [v.tolist() for v in self.vectors],
            "metadata": self.metadata
        }
        with open(self.persist_path, "w") as f:
            json.dump(data, f)

    def load(self):
        """Load state from local disk."""
        if os.path.exists(self.persist_path):
            with open(self.persist_path, "r") as f:
                data = json.load(f)
                if data["dimension"] != self.dimension:
                    raise ValueError("Stored dimension mismatch!")
                self.vectors = [np.array(v, dtype=np.float32) for v in data["vectors"]]
                self.metadata = data["metadata"]