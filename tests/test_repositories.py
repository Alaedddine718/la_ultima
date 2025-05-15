import os
from repositories.encuesta_repo import EncuestaRepository

def test_guardar_y_cargar_encuesta_tmp():
    ruta = "data/test_encuestas.json"

    if os.path.exists(ruta):
        os.remove(ruta)

    repo = EncuestaRepository(ruta_archivo=ruta)

    encuesta_dict = {
        "id": "123",
        "pregunta": "¿Pizza o hamburguesa?",
        "opciones": ["Pizza", "Hamburguesa"],
        "votos": {},
        "estado": "activa",
        "timestamp_inicio": "2025-05-15T00:00:00",
        "duracion_segundos": 30,
        "tipo": "simple"
    }

    repo.guardar_encuesta(encuesta_dict)
    resultado = repo.cargar_todas()

    assert isinstance(resultado, list)
    assert resultado[0]["id"] == "123"

    if os.path.exists(ruta):
        os.remove(ruta)
