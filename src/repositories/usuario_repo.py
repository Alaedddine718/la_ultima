import json
import os

class UsuarioRepository:
    def __init__(self, ruta_archivo="data/usuarios.json"):
        self.ruta = ruta_archivo
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists(self.ruta):
            with open(self.ruta, "w") as f:
                json.dump([], f)

    
