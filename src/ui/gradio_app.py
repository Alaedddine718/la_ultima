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

# Inicialización de servicios y controlador
def lanzar_ui():
    config = cargar_config()

    encuesta_repo = crear_encuesta_repo()
    usuario_repo = crear_usuario_repo()
    nft_repo = crear_nft_repo()

    poll_service = PollService(encuesta_repo)
    user_service = UserService(usuario_repo)
    nft_service = NFTService(nft_repo)
    chatbot_service = ChatbotService(config["modelo_chatbot"])

    ui_controller = UIController(poll_service, user_service, nft_service, chatbot_service)

    def procesar_mensaje(mensaje, username):
        if not mensaje or not username:
            return "Por favor, ingresa un mensaje y tu nombre."
        return ui_controller.responder_chat(username, mensaje)

    def ver_tokens(username):
        if not username:
            return "Por favor, introduce tu nombre de usuario."
        tokens = ui_controller.ver_tokens_usuario(username)
        if not tokens:
            return "No se encontraron tokens."
        return "\n".join([str(token) for token in tokens])

    with gr.Blocks(title="Plataforma de Votaciones para Streamers") as interfaz:
        gr.Markdown("# Plataforma de Votaciones para Streamers")

        with gr.Row():
            mensaje_input = gr.Textbox(label="Escribe un mensaje", placeholder="mensaje")
            respuesta_output = gr.Textbox(label="Respuesta del sistema")

        with gr.Row():
            usuario_input = gr.Textbox(label="Usuario")
            ver_btn = gr.Button("Ver mis tokens")

        with gr.Row():
            enviar_btn = gr.Button("Enviar")
            limpiar_btn = gr.Button("Limpiar")

        enviar_btn.click(
            fn=procesar_mensaje,
            inputs=[mensaje_input, usuario_input],
            outputs=respuesta_output
        )

        ver_btn.click(
            fn=ver_tokens,
            inputs=usuario_input,
            outputs=respuesta_output
        )

        limpiar_btn.click(
            fn=lambda: ("", ""),
            inputs=[],
            outputs=[mensaje_input, respuesta_output]
        )

    interfaz.launch(server_port=config["puerto_ui"])



















