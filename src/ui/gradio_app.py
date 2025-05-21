import gradio as gr
from src.services.user_service import UserService
from src.services.nft_service import NFTService
from src.services.poll_service import PollService
from src.services.chatbot_service import ChatbotService
from src.repositories.usuario_repo import crear_usuario_repo
from src.repositories.nft_repo import crear_nft_repo
from src.repositories.encuesta_repo import crear_encuesta_repo
from src.controllers.ui_controller import UIController
from src.config import config


def lanzar_ui():
    # Repositorios
    usuario_repo = crear_usuario_repo()
    nft_repo = crear_nft_repo()
    encuesta_repo = crear_encuesta_repo()

    # Servicios
    user_service = UserService(usuario_repo)
    nft_service = NFTService(nft_repo, config)
    poll_service = PollService(encuesta_repo, config)
    chatbot_service = ChatbotService(config["modelo_chatbot"])

    # Controlador
    controller = UIController(poll_service, user_service, nft_service, chatbot_service)

    # Funciones para la interfaz
    def registrar_usuario(username, password):
        return controller.registrar_usuario(username, password)

    def iniciar_sesion(username, password):
        return controller.iniciar_sesion(username, password)

    def enviar_mensaje(username, mensaje):
        return controller.responder_chat(username, mensaje)

    def ver_tokens(username):
        return controller.ver_tokens_usuario(username)

    # Interfaz
    with gr.Blocks() as demo:
        with gr.Tab("Autenticación"):
            with gr.Row():
                username = gr.Textbox(label="Usuario")
                password = gr.Textbox(label="Contraseña", type="password")
            with gr.Row():
                btn_registrar = gr.Button("Registrarse")
                btn_login = gr.Button("Iniciar sesión")
            resultado = gr.Textbox(label="Resultado")

            btn_registrar.click(fn=registrar_usuario, inputs=[username, password], outputs=resultado)
            btn_login.click(fn=iniciar_sesion, inputs=[username, password], outputs=resultado)

        with gr.Tab("Chat"):
            with gr.Row():
                mensaje = gr.Textbox(label="Escribe un mensaje")
                usuario = gr.Textbox(label="Usuario")
            btn_enviar = gr.Button("Enviar")
            respuesta = gr.Textbox(label="Respuesta del sistema")
            btn_enviar.click(fn=enviar_mensaje, inputs=[usuario, mensaje], outputs=respuesta)

            btn_tokens = gr.Button("Ver mis tokens")
            tokens = gr.Textbox(label="Mis Tokens")
            btn_tokens.click(fn=ver_tokens, inputs=usuario, outputs=tokens)

    demo.launch(server_port=config["puerto_ui"])























