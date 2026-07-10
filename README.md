# PadmaDB 🪷

**A blazing-fast, lightweight in-memory vector database built in pure Python and NumPy.**

[![PyPI version](https://img.shields.io/pypi/v/padmadb.svg?color=blue)](https://pypi.org/project/padmadb/)
[![Python Supported](https://img.shields.io/pypi/pyversions/padmadb.svg)](https://pypi.org/project/padmadb/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Pinecone, Milvus, and Weaviate are incredible for enterprise-scale billions of vectors. But when you are building local AI apps, testing RAG pipelines, or running lightweight microservices, spinning up a massive cloud infrastructure is overkill.

**PadmaDB** solves this by providing a hyper-fast, zero-dependency (beyond NumPy/FastAPI) vector search engine that runs locally and persists to disk.

---

## 🚀 Features

* **Pure Python/NumPy Engine:** No C++ compilers, Docker containers, or cloud APIs required.
* **Exact Nearest Neighbor (k-NN):** Guarantees 100% recall using optimized float32 Cosine Similarity matrix multiplications.
* **RESTful Architecture:** Ships with a built-in FastAPI server, allowing it to act as an independent microservice database.
* **Local Persistence:** Automatically serializes vector state to your local disk.

---

## 📦 Installation

```bash
pip install padmadb
```

---

## ⚡ Quickstart

### 1. Start the Database Server
You can launch the server locally in just a few lines of code:

```python
from padmadb.server import run_server

if __name__ == "__main__":
    # Runs the database engine on [http://0.0.0.0:8000](http://0.0.0.0:8000)
    run_server()
```

### 2. Connect and Query (Client SDK)
In a separate Python script or Jupyter Notebook, connect to your local PadmaDB instance to insert and search vectors.

```python
from padmadb import PadmaClient

# Initialize client
client = PadmaClient(host="http://localhost:8000")

# Insert a 384-dimensional vector (e.g., from all-MiniLM-L6-v2)
vector_data = [0.12, -0.45, 0.88] # Truncated for example; must be length 384
client.insert(
    vec_id="doc_1", 
    vector=vector_data, 
    metadata={"text": "Machine learning is fascinating."}
)

# Search for the Top-K nearest neighbors
results = client.search(vector=vector_data, top_k=1)
print(results)
```

---

## 🧠 Architecture & Roadmap

PadmaDB currently utilizes a brute-force exact search mechanism tailored for datasets up to 100,000 vectors, where in-memory matrix multiplication is effectively instantaneous.

**Upcoming in v0.2.x:**
* Implementation of `threading.Lock()` for concurrent write-safety.
* Transition from JSON persistence to memory-mapped `.npy` binary arrays for faster cold boots.
* HNSW (Hierarchical Navigable Small World) indexing for billion-scale querying with O(log N) search times.

---

## 🤝 Contributing

PadmaDB is fully open-source. We warmly welcome collaborators, researchers, and cloners! 

Want to help build the ultimate local AI database? **Clone the repo, fork it, break it, fix it, and submit a PR!**
