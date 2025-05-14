import praw
import pandas as pd
from pathlib import Path
import time


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


def load_keywords(file_path="keywords.txt"):
    """Load keywords from a text file."""
    with open(file_path, "r") as file:
        keywords = [line.strip() for line in file.readlines() if line.strip()]
    print(f"Loaded {len(keywords)} keywords.")
    return keywords


def crawl_all_posts_by_keyword(reddit, keyword, limit_per_page=100, known_ids=None):
    """Crawl all available posts for a given keyword using PRAW's pagination."""
    all_posts = []
    known_ids = known_ids or set()  # Use a set to track known post IDs
    
    try:
        print(f"Searching for all posts with keyword: '{keyword}'...")
        # Initialize the search
        search_results = reddit.subreddit("all").search(
            keyword, sort="relevance", limit=limit_per_page
        )

        # Loop through pages of results
        while True:
            batch = list(search_results)
            if not batch:
                break
            
            for post in batch:
                # Check for duplicate posts
                if post.id in known_ids:
                    continue
                
                # Add post data
                post_data = {
                    "id": post.id,
                    "title": post.title,
                    "selftext": post.selftext if post.selftext else "",
                    "subreddit": post.subreddit.display_name,
                    "score": post.score,
                    "url": post.url,
                    "created_utc": post.created_utc,
                    "upvote_ratio": post.upvote_ratio,
                    "num_comments": post.num_comments,
                    "keyword": keyword  # Add keyword to track the search term
                }
                all_posts.append(post_data)
                known_ids.add(post.id)

            # Move to the next page
            after = batch[-1].name
            search_results = reddit.subreddit("all").search(
                keyword, sort="relevance", limit=limit_per_page, params={"after": after}
            )
            time.sleep(1)  # Be polite to the API
            
        print(f"Collected {len(all_posts)} unique posts for keyword: '{keyword}'")
    except Exception as e:
        print(f"Error crawling keyword '{keyword}': {e}")

    return all_posts, known_ids


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
    
    # Load keywords from the provided file
    keywords = load_keywords("keywords.txt")

    # Crawl posts using the loaded keywords
    all_posts = []
    known_ids = set()
    for keyword in keywords:
        keyword_posts, known_ids = crawl_all_posts_by_keyword(reddit, keyword, limit_per_page=100, known_ids=known_ids)
        all_posts.extend(keyword_posts)

    # Save crawled posts to data/posts.csv
    save_posts(all_posts, output_path="data/posts.csv")


if __name__ == "__main__":
    main()
