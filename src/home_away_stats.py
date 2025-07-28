import pandas as pd
from data_processing import load_matches
from team_stats import add_result_columns


def summarize_home_away(df: pd.DataFrame) -> pd.DataFrame:
    """Break down performance for home and away matches."""
    df = add_result_columns(df)
    summary = df.groupby(['team', 'season', 'venue']).agg(
        matches=('result', 'count'),
        wins=('result', lambda x: (x == 'win').sum()),
        draws=('result', lambda x: (x == 'draw').sum()),
        losses=('result', lambda x: (x == 'loss').sum()),
        goals_for=('goals_for', 'sum'),
        goals_against=('goals_against', 'sum'),
        points=('points', 'sum'),
    ).reset_index()
    summary['win_pct'] = (summary['wins'] / summary['matches']).round(3)
    return summary


if __name__ == "__main__":
    matches = load_matches()
    summary = summarize_home_away(matches)
    summary.to_csv("data/home_away_stats.csv", index=False)
    print("✅ Saved: data/home_away_stats.csv")
