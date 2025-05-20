from src.repositories.encuesta_repo import EncuestaRepository

class EncuestaRepositoryNeo4j(EncuestaRepository):
    def __init__(self, uri, user, password):
        self.encuestas = {}  # Simulación local

    def guardar_encuesta(self, encuesta_dict):
        self.encuestas[encuesta_dict["id"]] = encuesta_dict

    def obtener_encuesta(self, encuesta_id):
        return self.encuestas.get(encuesta_id)
