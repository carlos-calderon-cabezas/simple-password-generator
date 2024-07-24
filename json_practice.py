import json

with open("data.json", mode="r") as data_file:
    data = json.load(data_file)
    print(data["Amazon"])
