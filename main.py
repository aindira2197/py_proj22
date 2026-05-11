teams = [
    {"name": "Barcelona", "points": 85},
    {"name": "Real Madrid", "points": 90},
    {"name": "Liverpool", "points": 78},
    {"name": "Milan", "points": 70}
]

winner = teams[0]

for team in teams:
    if team["points"] > winner["points"]:
        winner = team

print("Chempion:", winner["name"])

for team in teams:
    print(team["name"], "-", team["points"])

total = 0

for team in teams:
    total += team["points"]

average = total / len(teams)

print("O'rtacha ochko:", average)
