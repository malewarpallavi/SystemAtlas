# SystemAtlas

Software architecture analysis platform: understand and navigate complex codebases using repository scanning, dependency graphs, and Hybrid RAG.

## Problem

Large codebases are hard to understand. Developers struggle to see how services depend on each other and what a change might break. SystemAtlas scans repositories and dependencies, builds an architecture map, and answers questions about it using both graph and vector retrieval.

## Features

- Repository scanning and dependency analysis
- Architecture graph stored in Neo4j
- Hybrid RAG: Neo4j graph retrieval + Qdrant vector search + LLMs
- Contextual architecture analysis and impact assessment
- REST APIs with a microservices-oriented backend (PostgreSQL for application data)

## Architecture

```
Repository  -->  Scanner / Dependency Analyzer  -->  PostgreSQL (metadata)
                          |
                          +--> Neo4j (dependency graph)
                          +--> Qdrant (code/doc embeddings)
                                   |
User question --> Hybrid retrieval (graph + vector) --> LLM --> Answer
```

## Tech stack

[Backend: ...] · [Frontend: ...] · PostgreSQL · Neo4j · Qdrant · [LLM provider: ...]

## Getting started

```bash
git clone https://github.com/malewarpallavi/SystemAtlas.git
cd SystemAtlas
cp .env.example .env     # add your own keys
[commands to start the services]
```

## My contribution

[2-3 lines on exactly what you built, e.g. backend services, the RAG pipeline, graph schema]

## Roadmap

- [ ] Gemini integration via Google ADK
- [ ] Deployment on Google Cloud Run

## Author

Pallavi Malewar
