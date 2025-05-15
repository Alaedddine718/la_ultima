import pytest
from models.encuesta import Encuesta

def test_creacion_encuesta():
    e = Encuesta("¿Te gusta Python?", ["Sí", "No"], 10)
    assert e.pregunta == "¿Te gusta Python?"
    assert e.opciones == ["Sí", "No"]
    assert e.estado == "activa"


