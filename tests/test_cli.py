from controllers.cli_controller import CLIController
from services.poll_service import PollService
from services.user_service import UserService
from services.nft_service import NFTService

class DummyRepo:
    def __init__(self):
        self.data = []

    def guardar_encuesta(self, e): self.data.append(e)
    def cargar_todas(self): return self.data

class DummyNFTRepo:
    def __init__(self): self.tokens = []
    def guardar_token(self, t): self.tokens.append(t)
    def cargar_todos(self): return self.tokens


