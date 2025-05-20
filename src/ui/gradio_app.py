import gradio as gr

from src.services.poll_service import PollService
from src.services.user_service import UserService
from src.services.nft_service import NFTService
from src.services.chatbot_service import ChatbotService

from src.repositories.encuesta_repo import EncuestaRepository
from src.repositories.usuario_repo import crear_usuario_repo
from src.repositories.nft_repo import crear_nft_repo

from src.controllers.ui_controller import UIController

# Inicialización de servicios y controlador
def lanzar_ui():
    encuesta_repo = EncuestaRepository()
    usuario_repo = crear_usuario_repo()
    nft_repo = crear_nft_repo()

    poll_service = PollService(encuesta_repo)
    user_service = UserService(usuario_repo)
    nft_service = NFTService(nft_repo)
    chatbot_service = ChatbotService()

    ui_controller = UIController(poll_service, user_service, nft_service, chatbot_service)

    def manejar_mensaje(mensaje, username):
        return ui_controller.responder_chat(username, mensaje)

    def ver_mis_tokens(username):
        return str(ui_controller.ver_tokens_usuario(username))

    with gr.Blocks(title="Plataforma de Votaciones para Streamers") as interfaz:
        gr.Markdown("# Plataforma de Votaciones para Streamers")

        with gr.Row():
            mensaje = gr.Textbox(label="Escribe un mensaje")
            respuesta = gr.Textbox(label="Respuesta del sistema")

        with gr.Row():
            usuario = gr.Textbox(label="Usuario")
            tokens_btn = gr.Button("Ver mis tokens")

        with gr.Row():
            enviar_btn = gr.Button("Enviar")
            limpiar_btn = gr.Button("Limpiar")

        enviar_btn.click(fn=manejar_mensaje, inputs=[mensaje, usuario], outputs=[respuesta])
        limpiar_btn.click(fn=lambda: ("", ""), outputs=[mensaje, respuesta])
        tokens_btn.click(fn=ver_mis_tokens, inputs=[usuario], outputs=[respuesta])

    interfaz.launch(server_port=7860)
















