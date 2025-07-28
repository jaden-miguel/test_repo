import sys
from pathlib import Path
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))
from home_away_stats import summarize_home_away


def test_summarize_home_away():
    data = [
        {"team": "A", "season": "2022-23", "goals_for": 2, "goals_against": 1, "venue": "home"},
        {"team": "A", "season": "2022-23", "goals_for": 1, "goals_against": 1, "venue": "away"},
        {"team": "A", "season": "2022-23", "goals_for": 0, "goals_against": 1, "venue": "away"},
    ]
    df = pd.DataFrame(data)
    summary = summarize_home_away(df)
    home = summary[(summary.team == "A") & (summary.venue == "home")]
    away = summary[(summary.team == "A") & (summary.venue == "away")]
    assert float(home.win_pct) == 1.0
    assert float(away.win_pct) == 0.0
