import pytest
from services.poll_service import PollService

class FakeRepo:
    def __init__(self):
        self.data = []

    def guardar_encuesta(self, encuesta_dict):
        self.data.append(encuesta_dict)

    def cargar_todas(self):
        return self.data



