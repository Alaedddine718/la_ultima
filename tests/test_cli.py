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

def test_cli_controller_crea_encuesta():
    encuesta_repo = DummyRepo()
    user_repo = DummyRepo()
    nft_repo = DummyNFTRepo()

    poll_service = PollService(encuesta_repo)
    user_service = UserService(user_repo)
    nft_service = NFTService(nft_repo)

    cli = CLIController(poll_service, user_service, nft_service)

    cli.ejecutar_comando("crear_encuesta ¿Te gusta Python? Sí,No 30")

    encuestas = encuesta_repo.cargar_todas()
    assert len(encuestas) == 1
    assert encuestas[0]["pregunta"] == "¿Te gusta Python?"
