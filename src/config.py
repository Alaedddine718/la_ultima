import json

def cargar_config():
    with open("config.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)
