import pytest
from services.poll_service import PollService

class FakeRepo:
    def __init__(self):
        self.data = []

    def guardar_encuesta(self, encuesta_dict):
        self.data.append(encuesta_dict)

    def cargar_todas(self):
        return self.data

def test_crear_y_votar_encuesta():
    repo = FakeRepo()
    service = PollService(repo)

    encuesta_id = service.crear_encuesta("¿Café o té?", ["Café", "Té"], 60)
    resultados = service.votar(encuesta_id, "usuario1", "Café")

    assert resultados["Café"] == 1

def test_voto_duplicado():
    repo = FakeRepo()
    service = PollService(repo)

    encuesta_id = service.crear_encuesta("¿Café o té?", ["Café", "Té"], 60)
    service.votar(encuesta_id, "usuario1", "Café")

    with pytest.raises(Exception):
        service.votar(encuesta_id, "usuario1", "Té")

