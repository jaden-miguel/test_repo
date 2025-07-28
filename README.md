# ⚽ Premier League Team Performance (2022–2024)

This project analyzes English Premier League team performance across the 2022/23 and 2023/24 seasons using open match data. It goes beyond basic point totals by tracking team Elo ratings over time and comparing home vs away performance.

Designed for analysts who want a clean example of fetching live data, processing it with Pandas, and building interactive charts with Plotly. A small command-line interface lets you run the entire pipeline with a single command.

---

## Features

- Pulls match data from [openfootball](https://github.com/openfootball/football.json)
- Calculates total league points for each team
- Compares seasons 2022/23 vs 2023/24
- Interactive Plotly bar chart
- Clean Python modules (no notebooks)
- Tracks team Elo rating progression
- Home vs away breakdown and per-venue stats
- Interactive Plotly line chart of top teams' Elo ratings
- Detailed team stats (wins, draws, goal difference, win percentage)
- Simple CLI to run the full analysis pipeline
- Minimal unit tests with pytest

---

## 📁 Project Structure

```
soccer-performance-23-24/
├── data/
│   ├── matches.json           ← Raw match results
│   ├── team_points.csv        ← Aggregated points per team/season
│   ├── team_elo.csv           ← Elo rating after each match
│   ├── final_elo.csv          ← Final Elo rating per team
│   ├── team_stats.csv         ← Extended statistics per team/season
│   └── home_away_stats.csv    ← Home vs away performance
├── src/
│   ├── data_fetch.py          ← Downloads match data
│   ├── data_processing.py     ← Cleans and aggregates data
│   ├── analysis.py            ← Generates final summary CSV
│   ├── elo_rating.py          ← Elo calculation helpers
│   ├── team_stats.py          ← Additional stats computation
│   ├── home_away_stats.py     ← Home/away breakdown logic
│   ├── cli.py                 ← Command line interface
│   └── visualization.py       ← Builds interactive chart
├── assets/
│   └── example_output.png     ← Chart screenshot
├── requirements.txt           ← Python dependencies
└── README.md                  ← Project overview
```

---

## 🚀 Getting Started

### 1. Clone and Set Up

```bash
git clone <this-repo>.git
cd <this-repo>
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 2. Fetch and Process Data

Run everything with the CLI:

```bash
python src/cli.py all
```

Or run individual steps as needed:

```bash
python src/cli.py fetch
python src/cli.py process
python src/cli.py analyze
python src/cli.py stats
python src/cli.py homeaway
```

This will generate:

```
data/matches.json
data/team_points.csv
data/team_elo.csv
data/final_elo.csv
data/team_stats.csv
data/home_away_stats.csv
```

---

### 3. Visualize with Plotly

```bash
python src/cli.py viz
```

✅ Opens interactive charts: a grouped bar chart of points by season and a line plot of Elo rating trajectories for the top teams.

---

## 📷 Example Output

![Example Chart](assets/example_output.png)

---

## 🔧 Dependencies

Install everything with:

```bash
pip install -r requirements.txt
```

Key packages:

* `requests`
* `pandas`
* `plotly`

### Run Tests

```bash
pytest
```

---

## 🧠 What You’ll Learn

* Working with open football datasets
* Calculating match results and league points
* Season-to-season performance comparison
* Building an Elo rating model to track team strength
* Interactive storytelling with Plotly
* Clean code and folder structure

---

## 🪪 License

MIT License — feel free to use or extend for your own sports analytics projects.

---

## 🙌 Connect

If this project helps you, feel free to star ⭐ it or connect with me on GitHub!
