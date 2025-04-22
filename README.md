# Reddit-recommendation-system


# Reddit Recommendation System with IR + Web Agent

A smart recommendation system for Reddit that combines Information Retrieval techniques and Web Agent automation to deliver personalized, relevant content—helping users discover high-quality posts beyond their usual feed.

![Architecture](path/to/system_architecture.png)

## Features

- Semantic search over Reddit posts using embeddings or TF-IDF
- Personalized recommendations based on user interests or upvote history
- Web Agent to collect and update live Reddit data
- Web interface for query-based search and interaction
- Evaluation framework for measuring personalization quality

## Project Structure

```
reddit-recommender/
├── data/                 # Stored Reddit post data
├── src/                  # Core scripts: crawler, IR engine, personalization
│   ├── crawler.py
│   ├── ir_engine.py
│   ├── recommend.py
│   └── evaluate.py
├── app/                  # Streamlit app
│   └── app.py
├── demo_notebooks/       # Interactive walkthroughs
├── requirements.txt
├── README.md
└── system_architecture.png
```

## Web Demo

Run the Streamlit interface locally:

```bash
pip install -r requirements.txt
streamlit run app/app.py
```

### Interface Features:
- Input a search query (e.g., "AI in healthcare")
- View top Reddit post matches
- Filter by subreddit, recency, or user profile
- (Optional) Rate post relevance to improve personalization

## How It Works

1. Data Collection: Crawler pulls posts from Reddit via API.
2. IR Pipeline: Text is vectorized using TF-IDF or embeddings (e.g., OpenAI or SBERT).
3. Ranking: Similarity scores computed for each post (cosine similarity or BM25).
4. Personalization Layer: Re-ranks posts based on a user’s history or simulated preferences.
5. Interface: Streamlit app enables querying, filtering, and interaction.
6. Evaluation: Offline metrics (NDCG, diversity) and mock feedback used to assess personalization quality.

## Evaluation: Measuring Personalization

- Offline: Run `evaluate.py` using mock user profiles
- Metrics: NDCG, Personalization@K, Intra-list diversity, Serendipity
- Comparison: Personalized vs. non-personalized outputs
- User Study (optional): Ask users to rate result sets

## Example Commands

```bash
# Recommend posts based on a query
python src/recommend.py --query "best LLMs for education" --top_k 5

# Recommend based on user history
python src/recommend.py --user mock_user --mode history
```

## TODOs / Future Work

- [ ] Deploy Streamlit app to HuggingFace Spaces
- [ ] Add feedback-based online learning loop
- [ ] Support subreddit recommendation
- [ ] Add caching layer for faster retrieval

## Author

Yile Wang  
M.S. in Data Science | NLP + IR + ML Engineer  
GitHub: [@arinwangyile](https://github.com/arinwangyile)


---

**6. Architecture Diagram**
![Reddit Recommendation System Architecture](A_schematic_diagram_illustrates_a_Reddit_Recommend.png)

