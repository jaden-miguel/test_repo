# ⚽ Premier League Team Performance (2022–2024)

This project analyzes English Premier League team performance across the 2022/23 and 2023/24 seasons using open match data. It goes beyond basic point totals by tracking team Elo ratings over time and comparing home vs away performance.


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
