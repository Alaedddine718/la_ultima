from patterns.factory import EncuestaFactory
from patterns.strategy import (
    EstrategiaAlfabetica,
    EstrategiaAleatoria,
    EstrategiaProrroga
)
from patterns.observer import Observable, Observador

def test_factory_crea_encuesta():
    encuesta = EncuestaFactory.crear_encuesta("Pregunta", ["Sí", "No"], 30)
    assert encuesta.pregunta == "Pregunta"
    assert "Sí" in encuesta.opciones

def test_estrategia_alfabetica():
    estrategia = EstrategiaAlfabetica()
    r = estrategia.resolver(["Zebra", "Árbol", "Beta"])
    assert r == "Beta"

def test_estrategia_aleatoria():
    estrategia = EstrategiaAleatoria()
    r = estrategia.resolver(["A", "B"])
    assert r in ["A", "B"]


