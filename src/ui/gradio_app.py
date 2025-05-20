import gradio as gr

from src.services.poll_service import PollService
from src.services.user_service import UserService
from src.services.nft_service import NFTService
from src.services.chatbot_service import ChatbotService

from src.repositories.encuesta_repo import crear_encuesta_repo
from src.repositories.usuario_repo import crear_usuario_repo
from src.repositories.nft_repo import crear_nft_repo

from src.controllers.ui_controller import UIController

def lanzar_ui():
    encuesta_repo = crear_encuesta_repo()
    usuario_repo = crear_usuario_repo()
    nft_repo = crear_nft_repo()

    poll_service = PollService(encuesta_repo)
    user_service = UserService(usuario_repo)
    nft_service = NFTService(nft_repo)
    chatbot_service = ChatbotService(poll_service)

    ui_controller = UIController(poll_service, user_service, nft_service, chatbot_service)

    with gr.Blocks(theme=gr.themes.Base()) as interfaz:
        gr.Markdown("# Plataforma de Votaciones para Streamers")

        with gr.Row():
            with gr.Column():
                mensaje_input = gr.Textbox(label="Escribe un mensaje", placeholder="mensaje")
                username_input = gr.Textbox(label="Usuario")
                boton_enviar = gr.Button("Enviar")
                boton_limpiar = gr.Button("Limpiar")
            with gr.Column():
                output = gr.Textbox(label="Respuesta del sistema")
                boton_ver_tokens = gr.Button("Ver mis tokens")

        def responder(mensaje, username):
            return ui_controller.responder_chat(username, mensaje)

        def ver_tokens(username):
            return ui_controller.ver_tokens_usuario(username)

        boton_enviar.click(fn=responder, inputs=[mensaje_input, username_input], outputs=output)
        boton_limpiar.click(fn=lambda: "", inputs=None, outputs=output)
        boton_ver_tokens.click(fn=ver_tokens, inputs=username_input, outputs=output)

    interfaz.launch()















