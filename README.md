"""
Build a SQLite database (movies.db) from data/movies.csv.

Run this once before starting the Flask app:

    python build_db.py
"""

import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "movies.csv")
DB_PATH = os.path.join(BASE_DIR, "movies.db")


def parse_votes(value):
    """Convert vote count strings (e.g. '1,234') to int, or None."""
    if pd.isna(value):
        return None
    try:
        return int(str(value).replace(",", "").strip())
    except (ValueError, TypeError):
        return None


def parse_duration_minutes(value):
    """Convert duration strings like '1 h 39 m' to total minutes, or None."""
    if pd.isna(value):
        return None
    text = str(value).strip()
    hours, minutes = 0, 0
    try:
        if "h" in text:
            parts = text.split("h")
            hours = int(parts[0].strip())
            text = parts[1] if len(parts) > 1 else ""
        text = text.replace("m", "").strip()
        if text:
            minutes = int(text)
        total = hours * 60 + minutes
        return total if total > 0 else None
    except (ValueError, IndexError):
        return None


def build_database(csv_path=CSV_PATH, db_path=DB_PATH):
    print(f"Reading: {csv_path}")
    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df)} rows.")

    out = pd.DataFrame()
    out["id"] = range(1, len(df) + 1)
    out["title"] = df["Title"].astype(str).str.strip()
    out["release_date"] = df["Release Date"].astype(str)
    out["description"] = df["Description"].astype(str)
    out["rating"] = pd.to_numeric(df["Rating"], errors="coerce")
    out["votes"] = df["No of Persons Voted"].apply(parse_votes)
    out["directed_by"] = df["Directed by"].fillna("").astype(str)
    out["written_by"] = df["Written by"].fillna("").astype(str)
    out["duration"] = df["Duration"].fillna("").astype(str)
    out["duration_minutes"] = df["Duration"].apply(parse_duration_minutes)
    out["genres"] = df["Genres"].fillna("").astype(str)

    # Drop rows without a title
    out = out[out["title"].str.len() > 0]
    out = out.drop_duplicates(subset="title", keep="first").reset_index(drop=True)
    out["id"] = range(1, len(out) + 1)

    print(f"Writing {len(out)} rows to: {db_path}")
    if os.path.exists(db_path):
        os.remove(db_path)

    conn = sqlite3.connect(db_path)
    out.to_sql("movies", conn, index=False, if_exists="replace")

    # Indexes for fast search/sort
    conn.execute("CREATE INDEX idx_movies_title ON movies(title)")
    conn.execute("CREATE INDEX idx_movies_rating ON movies(rating)")
    conn.execute("CREATE INDEX idx_movies_votes ON movies(votes)")
    conn.execute("CREATE INDEX idx_movies_release_date ON movies(release_date)")
    conn.commit()
    conn.close()

    print("Done.")


if __name__ == "__main__":
    build_database()
