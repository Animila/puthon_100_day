import pandas

data = pandas.read_csv("data_belock.csv")
grey_belock_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_belock_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_belock_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_belock_count)
print(cinnamon_belock_count)
print(black_belock_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_belock_count, cinnamon_belock_count, black_belock_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("belock_count.csv")