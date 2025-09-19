import pandas as pd
dataset = {
    'cars': ['BMW', 'Toyota', 'volvo'],
    'passing': [3, 7, 2]
}
myvar = pd.DataFrame(dataset)
print(myvar)

calories = {"day1": 240, "day2": 210, "day3":150}
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)

# DataFrame Examples
data = {
    "calories":[420, 380, 200],
    "duration": [50, 40, 45 ]
}
df = pd.DataFrame(data)
print(df )

df.to_csv('dataset.csv')
print(pd.read_csv('dataset.csv'))