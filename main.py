from scraper.competitor import fetch_competitor_posts
from scraper.reddit import fetch_reddit_posts
from scraper.hn import fetch_hn_posts
from datetime import datetime
import os

def save_markdown(posts, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Market Watch Report – {datetime.now().strftime('%Y-%m-%d')}\n\n")
        for post in posts:
            f.write(f"## {post['source']}\n")
            f.write(f"- [{post['title']}]({post['link']})\n")
            f.write(f"  - {post['summary']}\n\n")

def main():
    all_posts = (
        fetch_competitor_posts() +
        fetch_reddit_posts() +
        fetch_hn_posts()
    )
    os.makedirs("reports", exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    save_markdown(all_posts, f"reports/{today}.md")

if __name__ == "__main__":
    main()
