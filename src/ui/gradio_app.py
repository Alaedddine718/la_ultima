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

    poll_service = PollService(encuesta_repo)
    user_service = UserService(usuario_repo)
    nft_service = NFTService(nft_repo, config)
    chatbot_service = ChatbotService(config["modelo_chatbot"])

    controller = UIController(poll_service, user_service, nft_service, chatbot_service)

    with gr.Blocks() as interfaz:
        with gr.Tab("Autenticación"):
            usuario_auth = gr.Textbox(label="Usuario")
            contraseña_auth = gr.Textbox(label="Contraseña", type="password")
            resultado_auth = gr.Textbox(label="Resultado")
            btn_registro = gr.Button("Registrarse")
            btn_login = gr.Button("Iniciar sesión")

            btn_registro.click(controller.registrar_usuario, [usuario_auth, contraseña_auth], resultado_auth)
            btn_login.click(controller.iniciar_sesion, [usuario_auth, contraseña_auth], resultado_auth)

        with gr.Tab("Chat"):
            mensaje = gr.Textbox(label="Escribe un mensaje")
            usuario_chat = gr.Textbox(label="Usuario")
            respuesta = gr.Textbox(label="Respuesta del sistema")

            btn_enviar = gr.Button("Enviar")
            btn_limpiar = gr.Button("Limpiar")
            btn_tokens = gr.Button("Ver mis tokens")

            btn_enviar.click(controller.responder_chat, [usuario_chat, mensaje], respuesta)
            btn_limpiar.click(fn=lambda: "", outputs=respuesta)
            btn_tokens.click(controller.ver_tokens_usuario, usuario_chat, respuesta)

    interfaz.launch(server_port=config["puerto_ui"])
























