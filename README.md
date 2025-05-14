# 🔍 Reddit Tech Job-Related Post Recommendation System

Welcome to our Reddit Job Post Recommendation System — an intelligent search engine built for tech job seekers navigating Reddit. Instead of sifting through noisy posts or relying on Reddit's basic keyword matching, our system helps you **surface the most relevant job-related posts** using your custom list of interests.

## Motivation

Reddit is a powerful platform filled with job opportunities and discussions, but its native search is:

* 🔎 Primitive (exact keyword matches only)
* 😵‍💫 Noisy (irrelevant or outdated posts)
* 😞 Not designed for job seekers

**Our system fixes that** by:

* Reading a large curated list of job-related keywords from `keywords.txt`
* Scanning across multiple subreddits
* Extracting posts **only if they contain all the keyword terms anywhere in the post** (flexible AND precise)
* Providing clean results with **title**, **upvotes**, and **direct link** for review

## 🆚 Side-by-Side Comparison

| Feature                      | Reddit Native Search | Our System                                      |
| ---------------------------- | -------------------- | ----------------------------------------------- |
| Fuzzy Match Support          | ❌                    | ✅ (checks if all keywords are present anywhere) |
| Scans Multiple Subreddits    | ❌                    | ✅                                               |
| Structured Output            | ❌                    | ✅ (CSV or DataFrame)                            |
| Supports Large Keyword Lists | ❌                    | ✅ (over 400 custom terms)                       |
| Eliminates Redundancy        | ❌                    | ✅                                               |

### 🔎 Example Comparison (Screenshots)

#### Reddit Native Search for: `deep learning career`

![Reddit Search](./screenshots/reddit_native.png)

#### Our System Output for Same Query:

![Our System Output](./screenshots/our_system_output.png)

*(Notice how our system filters directly relevant posts with clean metadata and links!)*

---

## 📁 Project Structure

```
├── crawler.py              # Crawls Reddit for posts containing any keyword from keywords.txt
├── keywords.txt            # List of keywords used for job search
├── recommend.ipynb         # Jupyter notebook to refine, recommend, and visualize results
├── screenshots/            # Folder containing visual comparison images
```

---

## 🛠 How to Run

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/Reddit-recommendation-system.git
cd Reddit-recommendation-system
```

### 2. Set Up Python Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install praw pandas
```

### 3. Configure Reddit API

Edit the `crawler.py` file and insert your Reddit API credentials:

```python
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_SECRET",
    user_agent="recommendation-script"
)
```

You can register your app here: [Reddit Apps](https://www.reddit.com/prefs/apps)

### 4. Run the Crawler

```bash
python crawler.py
```

You’ll get a structured CSV/printout of all relevant posts!

### 5. Post-processing & Recommendation

Open the notebook:

```bash
jupyter notebook recommend.ipynb
```

Use it to filter by subreddit, visualize keyword heatmaps, and customize top picks.

---

## 💡 Future Work

* Integrate sentence embeddings for smarter relevance scoring
* Add time-based filtering (e.g., last week only)
* Build a web dashboard to browse and bookmark job posts



