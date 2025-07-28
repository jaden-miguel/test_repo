import os
import json
import requests

# Seasons we care about
SEASONS = ["2022-23", "2023-24"]
BASE_URL = "https://raw.githubusercontent.com/openfootball/football.json/master/{season}/en.1.json"

os.makedirs("data", exist_ok=True)


def fetch_season(season: str) -> list:
    """Download match data for a given Premier League season."""
    url = BASE_URL.format(season=season)
    print(f"\n📦 Fetching {season} data...")
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return data.get("matches", [])


all_matches = []
for season in SEASONS:
    matches = fetch_season(season)
    for match in matches:
        match["season"] = season
    all_matches.extend(matches)

with open("data/matches.json", "w") as f:
    json.dump(all_matches, f, indent=2)

print("\n✅ Saved: data/matches.json")
