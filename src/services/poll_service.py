class PollService:
    def __init__(self, encuesta_repo):
        self.encuesta_repo = encuesta_repo

    def crear_encuesta(self, pregunta, opciones, creador, duracion):
        encuesta = {
            "pregunta": pregunta,
            "opciones": opciones,
            "creador": creador,
            "duracion": duracion
        }
        self.encuesta_repo.guardar_encuesta(encuesta)

    def votar(self, encuesta_id, username, opcion):
        self.encuesta_repo.votar(encuesta_id, username, opcion)

    def obtener_resultados(self, encuesta_id):
        return self.encuesta_repo.obtener_resultados(encuesta_id)

    def encuestas_activas(self):
        return self.encuesta_repo.obtener_encuestas_activas()

