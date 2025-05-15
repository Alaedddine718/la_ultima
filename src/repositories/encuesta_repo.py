import json
import os

class EncuestaRepository:
    def __init__(self, ruta_archivo="data/encuestas.json"):
        self.ruta = ruta_archivo
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists(self.ruta):
            with open(self.ruta, "w") as f:
                json.dump([], f)

    def guardar_encuesta(self, encuesta_dict):
        encuestas = self.cargar_todas()
        encuestas.append(encuesta_dict)
        with open(self.ruta, "w") as f:
            json.dump(encuestas, f, indent=4)

    def cargar_todas(self):
        with open(self.ruta, "r") as f:
            return json.load(f)
