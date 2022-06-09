import pandas

data = pandas.read_csv("Day25/Squirrel_Census.csv")

gray_fur = data[data["Primary Fur Color"] == "Gray"]
cinnamon_fur = data[data["Primary Fur Color"] == "Cinnamon"]
black_fur = data[data["Primary Fur Color"] == "Black"]

gray_fur_count = gray_fur["Primary Fur Color"].count()
cinnamon_fur_count = cinnamon_fur["Primary Fur Color"].count()
black_fur_count = black_fur["Primary Fur Color"].count()

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_fur_count, cinnamon_fur_count, black_fur_count]
}

count_data = pandas.DataFrame(data_dict)

count_data.to_csv("Day25/squirrel_count.csv")