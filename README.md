# Reddit Advice Graph: Life Decision AI

GraphRAG-powered career advice system built from Reddit discussions using LLM extraction, knowledge graphs, semantic similarity, and graph-based retrieval.

---

## Project Overview

People often go to Reddit for advice about:

- careers
- layoffs
- burnout
- salary negotiations
- career switching
- job searching

However, the information is buried inside large amounts of unstructured text.

This project transforms Reddit career discussions into a structured knowledge graph that can be queried using natural language.

The system extracts:
- problem types
- roles
- constraints
- advice
- outcomes
- sentiment

and connects them using graph relationships and semantic similarity.

---

## Features

- Reddit career advice scraping
- LLM-powered structured extraction
- Knowledge graph construction
- GraphRAG-style Q&A pipeline
- Semantic similarity retrieval
- Streamlit app prototype
- Outcome sentiment analysis

---

## Tech Stack

### Languages & Libraries
- Python
- NetworkX
- Pandas
- Streamlit

### AI / NLP
- OpenAI GPT-4o-mini
- OpenAI Embeddings
- GraphRAG concepts
- Semantic similarity search

### Data Sources
- Reddit API / Reddit JSON endpoints

---

## Dataset Summary

- 1,897 Reddit career posts processed
- 10,946 graph nodes
- 12,451 graph edges

### Node Types
- CareerSituation
- ProblemType
- Role
- Constraint
- Advice
- Outcome

### Edge Types
- HAS_PROBLEM
- CURRENTLY_IN
- TARGETING
- FACES_CONSTRAINT
- HAS_ADVICE
- LEADS_TO
- SIMILAR_SITUATION

---

## Pipeline Architecture

### Phase 1 — Data Collection
Scraped career-related Reddit posts from:
- r/cscareerquestions
- r/careerguidance
- r/ITCareerQuestions
- r/learnprogramming
- r/financialindependence

### Phase 2 — LLM Extraction
Used GPT-4o-mini to transform raw Reddit text into structured JSON.

### Phase 3 — Knowledge Graph
Constructed a graph using NetworkX and semantic similarity embeddings.

### Phase 4 — GraphRAG Q&A
Implemented retrieval + graph traversal for grounded AI responses.

### Phase 5 — Streamlit Demo
Interactive UI for querying similar career situations and advice patterns.

---

## Example Query

### User Input
> “I want to switch from manufacturing to marketing.”

### System Output
- Similar situations
- Common constraints
- Advice patterns
- Outcome trends
- Actionable recommendations

---

## Repository Structure

```bash
reddit-advice-graph/
│
├── app.py
├── Final Group Project.ipynb
├── reddit_posts.csv
├── extracted_posts_clean.csv
├── extracted_posts_clean.json
├── outcome_posts.csv
├── graph_stats.json
├── career_graph.gpickle
└── Final Prezo - Unstructured Data.pptx
```

---

## Contributors

- Harelle
- Jenn
- Leslieane
- David
- Aryan

---

## Future Improvements

- Expand to additional industries
- Improve graph similarity filtering
- Add Neo4j integration
- Deploy Streamlit app online
- Improve GraphRAG grounding

---

## Academic Context

Final project for an Unstructured Data course focused on:
- NLP
- LLM pipelines
- knowledge graphs
- semantic retrieval
- graph-based reasoning
