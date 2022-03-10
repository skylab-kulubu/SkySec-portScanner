import json

def jsonData(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data