import os
from repositories.encuesta_repo import EncuestaRepository

def test_guardar_y_cargar_encuesta_tmp():
    ruta = "data/test_encuestas.json"

    if os.path.exists(ruta):
        os.remove(ruta)

    repo = EncuestaRepository(ruta_archivo=ruta)

   