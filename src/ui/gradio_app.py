# src/ui/gradio_app.py
import sys
import os
sys.path.insert(0, os.path.abspath("src"))
from services.poll_service import PollService
from services.user_service import UserService
from services.nft_service import NFTService
from services.chatbot_service import ChatbotService

from repositories.encuesta_repo import EncuestaRepository
from repositories.usuario_repo import UsuarioRepository
from repositories.nft_repo import NFTRepository

from controllers.ui_controller import UIController
from config import cargar_config

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
    ui_controller.lanzar()

# main.py (fuera de src)
# Asegúrate de que main.py tenga esto:
# from ui.gradio_app import lanzar_ui
# if __name__ == "__main__":
#     lanzar_ui()







