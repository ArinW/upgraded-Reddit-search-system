# src/crawler.py

import praw
import pandas as pd
from pathlib import Path

def init_reddit_api():
    """Initialize PRAW Reddit API instance."""
    client_id = "9ZefuwleJrpgurFCMaFXeQ"
    client_secret = "JaFW1h2cytRnWuxc7Umyb7FtzK5iYQ"
    user_agent = "rec by u/Every_Profile8717"
    
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )
    return reddit

def crawl_subreddits(reddit, subreddits, limit=100):
    """Crawl posts from a list of subreddits with a limit."""
    all_posts = []

    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        print(f"Crawling r/{subreddit_name}...")
        subreddit_posts = []

        try:
            for post in subreddit.new(limit=limit):  
                post_data = {
                    "id": post.id,
                    "title": post.title,
                    "selftext": post.selftext if post.selftext else "",
                    "subreddit": subreddit_name,
                    "score": post.score,
                    "url": post.url,
                    "created_utc": post.created_utc
                }
                subreddit_posts.append(post_data)
            
            print(f"Successfully crawled {len(subreddit_posts)} posts from r/{subreddit_name}")
            all_posts.extend(subreddit_posts)
        except Exception as e:
            print(f"Error crawling r/{subreddit_name}: {e}")
            print("This might be due to authentication issues with your Reddit API credentials")

    return all_posts

def save_posts(posts, output_path="data/posts.csv"):
    """Save crawled posts into CSV format."""
    if not posts:
        print("No posts to save.")
        return
        
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(posts)
    df.to_csv(output_path, index=False)
    print(f"Saved {len(posts)} posts to {output_path}")

def main():
    # Initialize Reddit API connection
    reddit = init_reddit_api()
    
    # Set to read-only mode explicitly
    reddit.read_only = True
    
    # Check if authentication was successful
    try:
        print("Testing connection to Reddit API...")
        subreddits = reddit.subreddits.default(limit=1)
        for _ in subreddits:
            pass  # Just testing that we can retrieve data
        print("Connection successful!")
    except Exception as e:
        print(f"Authentication error: {e}")
        print("This likely means your Reddit API credentials are invalid or expired.")
        print("Please check your credentials at https://www.reddit.com/prefs/apps")
        return  # Exit if we can't connect

    # Define your target subreddits
    TARGET_SUBREDDITS = [
        "jobs",
        # "datascience",
        # "ArtificialIntelligence", 
        # "technology",
        # "learnmachinelearning"
    ]

    # Crawl posts from target subreddits
    posts = crawl_subreddits(reddit, TARGET_SUBREDDITS, limit=200)

    # Save crawled posts to data/posts.csv
    save_posts(posts, output_path="data/posts.csv")

if __name__ == "__main__":
    main()