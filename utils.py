import json

def jsonData(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data

#Json dosyasını işliyoruz çok bir şey yok 