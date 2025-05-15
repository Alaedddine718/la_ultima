class Usuario:
    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash  # contraseña cifrada
        self.tokens = []  # lista de tokens NFT que tiene este usuario

   
