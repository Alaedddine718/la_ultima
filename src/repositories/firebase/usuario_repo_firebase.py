from src.repositories.encuesta_repo import EncuestaRepository

class EncuestaRepositoryFirebase(EncuestaRepository):
    def __init__(self, firebase_key):
        self.encuestas = {}  # Simulación simple para pruebas

    def guardar_encuesta(self, encuesta_dict):
        self.encuestas[encuesta_dict["id"]] = encuesta_dict

    def obtener_encuesta(self, encuesta_id):
        return self.encuestas.get(encuesta_id)

