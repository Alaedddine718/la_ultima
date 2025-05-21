from src.repositories.encuesta_repo import EncuestaRepository

class EncuestaRepositoryDummy(EncuestaRepository):
    def __init__(self):
        self.encuestas = {}
        self.votos = {}

    def guardar_encuesta(self, encuesta_dict):
        encuesta_id = encuesta_dict.get("id") or str(len(self.encuestas) + 1)
        encuesta_dict["id"] = encuesta_id
        encuesta_dict["votos"] = {}
        self.encuestas[encuesta_id] = encuesta_dict

    def obtener_encuesta(self, encuesta_id):
        return self.encuestas.get(encuesta_id)

    def votar(self, encuesta_id, username, opcion):
        encuesta = self.encuestas.get(encuesta_id)
        if encuesta:
            encuesta["votos"][username] = opcion

    def obtener_resultados(self, encuesta_id):
        encuesta = self.encuestas.get(encuesta_id)
        if not encuesta:
            return {}
        resultados = {opcion: 0 for opcion in encuesta["opciones"]}
        for voto in encuesta["votos"].values():
            if voto in resultados:
                resultados[voto] += 1
        return resultados

    def obtener_encuestas_activas(self):
        return list(self.encuestas.values())