import json
import pickle
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Reddit Advice Graph",
    layout="wide"
)

st.title("Reddit Advice Graph — Career Decision Analysis")
st.caption("Interactive GraphRAG system for exploring career advice patterns from Reddit data.")

BASE_DIR = Path.cwd()


GRAPH_PATH = BASE_DIR / "career_graph(1).gpickle"
POSTS_JSON_PATH = BASE_DIR / "extracted_posts_clean(1).json"
EMBEDDINGS_PATH = BASE_DIR / "embeddings_cache(1).json"
GRAPH_STATS_PATH = BASE_DIR / "graph_stats(1).json"


@st.cache_data
def load_posts():
    with open(POSTS_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return pd.DataFrame(data)


@st.cache_data
def load_embeddings():
    with open(EMBEDDINGS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


@st.cache_data
def load_graph_stats():
    with open(GRAPH_STATS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


@st.cache_resource
def load_graph():
    with open(GRAPH_PATH, "rb") as f:
        return pickle.load(f)


posts_df = load_posts()
embeddings_cache = load_embeddings()
graph_stats = load_graph_stats()
career_graph = load_graph()

st.success("All project files loaded successfully.")
st.write("Posts loaded:", len(posts_df))
st.write("Graph nodes:", career_graph.number_of_nodes())
st.write("Graph edges:", career_graph.number_of_edges())
