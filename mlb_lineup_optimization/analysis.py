import pandas as pd
import pulp

df = pd.read_csv("reds_2025_batting.csv")
df = df[df["PA"] >= 100].reset_index(drop=True)

positions = list(range(1, 10))
players = df.index.tolist()

required_positions = {
    "C": 1,
    "1B": 1,
    "2B": 1,
    "3B": 1,
    "SS": 1,
    "OF": 3,
}

model = pulp.LpProblem("Constrained_Lineup", pulp.LpMaximize)

x = pulp.LpVariable.dicts(
    "assign",
    ((i, j) for i in players for j in positions),
    cat="Binary"
)

model += pulp.lpSum(
    df.loc[i, "wRC+"] * x[(i, j)]
    for i in players
    for j in positions
)

for j in positions:
    model += pulp.lpSum(x[(i, j)] for i in players) == 1

for i in players:
    model += pulp.lpSum(x[(i, j)] for j in positions) <= 1

for pos, count in required_positions.items():
    model += pulp.lpSum(
        x[(i, j)]
        for i in players
        for j in positions
        if df.loc[i, "Position"] == pos
    ) == count

model.solve()

for j in positions:
    for i in players:
        if pulp.value(x[(i, j)]) == 1:
            print(j, df.loc[i, "Player"], df.loc[i, "Position"], df.loc[i, "wRC+"])
