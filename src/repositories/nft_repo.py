import json
import os

class NFTRepository:
    def __init__(self, ruta_archivo="data/nfts.json"):
        self.ruta = ruta_archivo
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists(self.ruta):
            with open(self.ruta, "w") as f:
                json.dump([], f)
    
    def guardar_token(self, token_dict):
        tokens = self.cargar_todos()
        tokens.append(token_dict)
        with open(self.ruta, "w") as f:
            json.dump(tokens, f, indent=4)

    def cargar_todos(self):
        with open(self.ruta, "r") as f:
            return json.load(f)

    def transferir_token(self, token_id, nuevo_owner):
        tokens = self.cargar_todos()
        for token in tokens:
            if token["token_id"] == token_id:
                token["owner"] = nuevo_owner
                break
        with open(self.ruta, "w") as f:
            json.dump(tokens, f, indent=4)
