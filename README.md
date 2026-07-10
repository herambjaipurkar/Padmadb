## PadmaDB 🪷

A blazing-fast, lightweight in-memory vector database built in pure Python and NumPy.
Pinecone, Milvus, and Weaviate are incredible for enterprise-scale billions of vectors. But when you are building local AI apps, testing RAG pipelines, or running lightweight microservices, spinning up a massive cloud infrastructure is overkill.
PadmaDB solves this by providing a hyper-fast, zero-dependency (beyond NumPy/FastAPI) vector search engine that runs locally and persists to disk.

## 🚀 Features

Pure Python/NumPy Engine: No C++ compilers, Docker containers, or cloud APIs required.

Exact Nearest Neighbor (k-NN): Guarantees 100% recall using optimized float32 Cosine Similarity matrix multiplications.

RESTful Architecture: Ships with a built-in FastAPI server, allowing it to act as an independent microservice database.

Local Persistence: Automatically serializes vector state to your local disk.


## 📦 Installation
```bash
pip install padmadb
```


## ⚡ Quickstart
1. Start the Database Server
You can launch the server in one line of code:
```bash
from padmadb.server import run_server

if __name__ == "__main__":
    # Runs the database engine on [http://0.0.0.0:8000](http://0.0.0.0:8000)
    run_server()
```

2. Connect and Query (Client SDK)
In a separate Python script or Jupyter Notebook:
```bash
from padmadb import PadmaClient

client = PadmaClient(host="http://localhost:8000")
```


# 1. Insert a 384-dimensional vector (e.g., from all-MiniLM-L6-v2)
```bash
vector_data = [0.12, -0.45, 0.88, ...] # Must be length 384
client.insert(
    vec_id="doc_1", 
    vector=vector_data, 
    metadata={"text": "Machine learning is fascinating."}
)
```

# 2. Search for the Top-K nearest neighbors
```bash
results = client.search(vector=vector_data, top_k=1)
print(results)
```


## 🧠 Architecture & Roadmap

PadmaDB v0.1.0 utilizes a brute-force exact search mechanism  tailored for datasets up to 100,000 vectors where in-memory matrix multiplication is effectively instantaneous.

## Upcoming in v0.2.x:
Implementation of threading.Lock() for concurrent write-safety.
Transition from JSON persistence to memory-mapped .npy binary arrays for faster cold boots.
HNSW (Hierarchical Navigable Small World) indexing for  billion-scale querying.


## 🤝 Contributing
PadmaDB is fully open-source. We warmly welcome collaborators, researchers, and cloners! 

Clone the repo, fork it, break it, fix it, and submit a PR! Let's build the ultimate local AI database together.