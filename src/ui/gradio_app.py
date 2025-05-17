import gradio as gr
from controllers.ui_controller import UIController
from services.poll_service import PollService
from services.user_service import UserService
from services.nft_service import NFTService
from services.chatbot_service import ChatbotService
from repositories.encuesta_repo import EncuestaRepository
from repositories.usuario_repo import UsuarioRepository
from repositories.nft_repo import NFTRepository

def lanzar_ui():
    encuesta_repo = EncuestaRepository()
    usuario_repo = UsuarioRepository()
    nft_repo = NFTRepository()

    poll_service = PollService(encuesta_repo)
    user_service = UserService(usuario_repo)
    nft_service = NFTService(nft_repo)
    chatbot_service = ChatbotService(poll_service)

    ui_controller = UIController(poll_service, user_service, nft_service, chatbot_service)

    interfaz = gr.Interface(
        fn=lambda mensaje, usuario: ui_controller.responder_chat(usuario, mensaje),
        inputs=["text", "text"],
        outputs="text",
        title="Plataforma de Votaciones para Streamers",
        description="Escribe un mensaje y tu nombre de usuario"
    )

    interfaz.launch()








