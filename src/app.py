from services.poll_service import PollService
from services.user_service import UserService
from services.nft_service import NFTService
from services.chatbot_service import ChatbotService

from repositories.encuesta_repo import EncuestaRepository
from repositories.usuario_repo import UsuarioRepository
from repositories.nft_repo import NFTRepository

from controllers.cli_controller import CLIController
from controllers.ui_controller import UIController
from ui.gradio_app import GradioApp

from config import cargar_config

def main(modo="CLI"):
    config = cargar_config()

    encuesta_repo = EncuestaRepository()
    usuario_repo = UsuarioRepository()
    nft_repo = NFTRepository()

    poll_service = PollService(encuesta_repo)
    user_service = UserService(usuario_repo)
    nft_service = NFTService(nft_repo)
    chatbot_service = ChatbotService(poll_service)

    if modo.upper() == "UI":
        ui_controller = UIController(poll_service, user_service, nft_service, chatbot_service)
        gradio_app = GradioApp(ui_controller)
        gradio_app.lanzar()
    else:
        cli_controller = CLIController(poll_service, user_service, nft_service)
        cli_controller.ejecutar()

if __name__ == "__main__":
    # cambia "CLI" por "UI" si quieres lanzar Gradio
    main("CLI")
