class Usuario:
    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash  # contraseña cifrada
        self.tokens = []  # lista de tokens NFT que tiene este usuario
    def agregar_token(self, token):
        self.tokens.append(token)

    def transferir_token(self, token_id, nuevo_owner):
        for token in self.tokens:
            if token.token_id == token_id:
                token.owner = nuevo_owner
                self.tokens.remove(token)
                return token
        raise Exception("Token no encontrado")
   
