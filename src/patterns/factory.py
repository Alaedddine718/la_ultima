from models.encuesta import Encuesta

class EncuestaFactory:
    @staticmethod
    def crear_encuesta(pregunta, opciones, duracion_segundos, tipo="simple"):
        # Aquí puedes extender con subclases si hay tipos distintos
        return Encuesta(pregunta, opciones, duracion_segundos, tipo)
