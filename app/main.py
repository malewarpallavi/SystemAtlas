import os
from dotenv import load_dotenv
from fastapi import FastAPI
from neo4j import GraphDatabase
from qdrant_client import QdrantClient

load_dotenv()

app = FastAPI(title="SystemAtlas")

neo4j_driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI", "bolt://localhost:7687"),
    auth=("neo4j", os.getenv("NEO4J_PASSWORD")),
)
qdrant = QdrantClient(url=os.getenv("QDRANT_URL", "http://localhost:6333"))


@app.get("/health")
def health():
    status = {}
    try:
        neo4j_driver.verify_connectivity()
        status["neo4j"] = "ok"
    except Exception as e:
        status["neo4j"] = f"error: {e}"
    try:
        qdrant.get_collections()
        status["qdrant"] = "ok"
    except Exception as e:
        status["qdrant"] = f"error: {e}"
    return status