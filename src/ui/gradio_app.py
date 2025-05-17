import gradio as gr
from src.services.poll_service import PollService
from src.services.user_service import UserService
from src.services.nft_service import NFTService
from src.services.chatbot_service import ChatbotService

from src.repositories.encuesta_repo import EncuestaRepository
from src.repositories.usuario_repo import UsuarioRepository
from src.repositories.nft_repo import NFTRepository

from src.controllers.ui_controller import UIController
from src.config import cargar_config

def lanzar_ui():
    config = cargar_config()

    encuesta_repo = EncuestaRepository()
    usuario_repo = UsuarioRepository()
    nft_repo = NFTRepository()

    poll_service = PollService(encuesta_repo)
    user_service = UserService(usuario_repo)
    nft_service = NFTService(nft_repo)
    chatbot_service = ChatbotService(poll_service)

    ui_controller = UIController(poll_service, user_service, nft_service, chatbot_service)

    with gr.Blocks() as demo:
        ui_controller.mostrar_interfaz(demo)

    demo.launch(server_port=config["puerto_ui"])






