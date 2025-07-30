import pandas as pd
from data_processing import load_matches


POINTS = {
    'win': 3,
    'draw': 1,
    'loss': 0,
}


def add_result_columns(df: pd.DataFrame) -> pd.DataFrame:
    def result(row):
        if row.goals_for > row.goals_against:
            return 'win'
        elif row.goals_for < row.goals_against:
            return 'loss'
        return 'draw'

    df['result'] = df.apply(result, axis=1)
    df['points'] = df['result'].map(POINTS)
    return df


def summarize_team_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Compute goals for/against, goal difference and record per team/season."""
    df = add_result_columns(df)
    df['goal_diff'] = df['goals_for'] - df['goals_against']
    summary = df.groupby(['team', 'season']).agg(
        matches=('result', 'count'),
        wins=('result', lambda x: (x == 'win').sum()),
        draws=('result', lambda x: (x == 'draw').sum()),
        losses=('result', lambda x: (x == 'loss').sum()),
        goals_for=('goals_for', 'sum'),
        goals_against=('goals_against', 'sum'),
        goal_diff=('goal_diff', 'sum'),
        points=('points', 'sum'),
    ).reset_index()
    summary['win_pct'] = (summary['wins'] / summary['matches']).round(3)
    return summary


if __name__ == "__main__":
    matches = load_matches()
    stats = summarize_team_stats(matches)
    stats.to_csv("data/team_stats.csv", index=False)
    print("✅ Saved: data/team_stats.csv")
