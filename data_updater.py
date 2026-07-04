"""
MyOdyssey Data Updater
Runs via GitHub Actions on Mon & Fri at 10:00 AM to refresh article data.
"""

import json
import os
from datetime import datetime

# Add parent dir to path for module imports
import sys
sys.path.insert(0, os.path.dirname(__file__))

from modules.article_fetcher import get_weekly_top_articles, get_retrospective_articles


def update():
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(data_dir, exist_ok=True)

    print(f"[{datetime.now().isoformat()}] Starting data update...")

    # Fetch weekly articles
    print("Fetching weekly top articles...")
    weekly = get_weekly_top_articles(limit=10)
    print(f"  Found {len(weekly)} articles")

    # Save
    output = {
        "last_updated": datetime.now().isoformat(),
        "weekly_articles": weekly,
    }

    output_path = os.path.join(data_dir, "latest_research.json")
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print(f"Data saved to {output_path}")
    print("Update complete.")


if __name__ == "__main__":
    update()
