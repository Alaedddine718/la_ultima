import json
import gradio as gr
from src.services.poll_service import PollService
from src.services.user_service import UserService
from src.services.nft_service import NFTService
from src.services.chatbot_service import ChatbotService
from src.repositories.encuesta_repo import crear_encuesta_repo
from src.repositories.usuario_repo import crear_usuario_repo
from src.repositories.nft_repo import crear_nft_repo
from src.controllers.ui_controller import UIController
from src.config import cargar_config

def lanzar_ui():
    config = cargar_config()

    encuesta_repo = crear_encuesta_repo()
    usuario_repo = crear_usuario_repo()
    nft_repo = crear_nft_repo()

    poll_service = PollService(encuesta_repo)  # CORREGIDO
    user_service = UserService(usuario_repo)
    nft_service = NFTService(nft_repo, config)
    chatbot_service = ChatbotService(config["modelo_chatbot"])

    controller = UIController(poll_service, user_service, nft_service, chatbot_service)

    print("Interfaz lanzada correctamente.")


























