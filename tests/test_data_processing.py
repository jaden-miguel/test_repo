import sys
from pathlib import Path
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))
from data_processing import calculate_team_points


def test_calculate_team_points():
    data = [
        {'team': 'A', 'season': '2022-23', 'goals_for': 2, 'goals_against': 1},
        {'team': 'A', 'season': '2022-23', 'goals_for': 1, 'goals_against': 1},
        {'team': 'A', 'season': '2022-23', 'goals_for': 0, 'goals_against': 1},
    ]
    df = pd.DataFrame(data)
    summary = calculate_team_points(df)
    assert summary.loc[0, 'points'] == 4
