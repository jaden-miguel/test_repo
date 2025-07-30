# ⚽ Premier League Team Performance (2022–2024)

This project analyzes English Premier League team performance across the 2022/23 and 2023/24 seasons using open match data. It goes beyond basic point totals by tracking team Elo ratings over time and comparing home vs away performance.

Designed for analysts who want a clean example of fetching live data, processing it with Pandas, and building interactive charts with Plotly.

---

## 📦 Features

- ✅ Live match data from [openfootball](https://github.com/openfootball/football.json)
- ⏱️ Calculates total league points for each team
- 📊 Compares seasons 2022/23 vs 2023/24
- 📈 Interactive Plotly bar chart
- 🧹 Modular, clean codebase (no notebooks)
- ⭐ Tracks team Elo rating progression
- 📉 Home vs away breakdown ready for further analysis
- 📈 Interactive Plotly line chart of top teams' Elo ratings

---

## 📁 Project Structure

```
soccer-performance-23-24/
├── data/
│   ├── matches.json           ← Raw match results
│   ├── team_points.csv        ← Aggregated points per team/season
│   ├── team_elo.csv           ← Elo rating after each match
│   └── final_elo.csv          ← Final Elo rating per team
├── src/
│   ├── data_fetch.py          ← Downloads match data
│   ├── data_processing.py     ← Cleans and aggregates data
│   ├── analysis.py            ← Generates final summary CSV
│   ├── elo_rating.py          ← Elo calculation helpers
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

```bash
python src/data_fetch.py
python src/data_processing.py
python src/analysis.py
```

This will generate:

```
data/matches.json
data/team_points.csv
data/team_elo.csv
data/final_elo.csv
```

---

### 3. Visualize with Plotly

```bash
python src/visualization.py
```

✅ Opens interactive charts: a grouped bar chart of points by season and a line plot of Elo rating trajectories for the top teams.


## 🔧 Dependencies

Install everything with:

```bash
pip install -r requirements.txt
```

Key packages:

* `requests`
* `pandas`
* `plotly`

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
