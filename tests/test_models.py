import pytest
from models.encuesta import Encuesta

def test_creacion_encuesta():
    e = Encuesta("¿Te gusta Python?", ["Sí", "No"], 10)
    assert e.pregunta == "¿Te gusta Python?"
    assert e.opciones == ["Sí", "No"]
    assert e.estado == "activa"

def test_votar_encuesta():
    e = Encuesta("¿Te gusta Python?", ["Sí", "No"], 10)
    e.votar("usuario1", "Sí")
    assert e.votos["usuario1"] == "Sí"
    assert e.resultados["Sí"] == 1

def test_voto_duplicado_lanza_excepcion():
    e = Encuesta("¿Te gusta Python?", ["Sí", "No"], 10)
    e.votar("usuario1", "Sí")
    with pytest.raises(Exception):
        e.votar("usuario1", "No")
