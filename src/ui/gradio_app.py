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

    # Crear repositorios según config.json
    encuesta_repo = crear_encuesta_repo()
    usuario_repo = crear_usuario_repo()
    nft_repo = crear_nft_repo()

    # Crear servicios
    poll_service = PollService(encuesta_repo)
    user_service = UserService(usuario_repo)
    nft_service = NFTService(nft_repo)
    chatbot_service = ChatbotService(config["modelo_chatbot"])

    # Crear controlador
    ui_controller = UIController(poll_service, user_service, nft_service, chatbot_service)

    # Funciones conectadas a Gradio
    def enviar_mensaje(mensaje, usuario):
        return ui_controller.responder_chat(usuario, mensaje)

    def ver_tokens(usuario):
        return str(ui_controller.ver_tokens_usuario(usuario))

    # Interfaz Gradio
    with gr.Blocks(title="Plataforma de Votaciones para Streamers") as interfaz:
        gr.Markdown("# Plataforma de Votaciones para Streamers")

        with gr.Row():
            mensaje_input = gr.Textbox(label="Escribe un mensaje", placeholder="mensaje")
            respuesta_output = gr.Textbox(label="Respuesta del sistema")

        with gr.Row():
            usuario_input = gr.Textbox(label="Usuario")
            boton_ver_tokens = gr.Button("Ver mis tokens")

        with gr.Row():
            boton_enviar = gr.Button("Enviar")
            boton_limpiar = gr.Button("Limpiar")

        boton_enviar.click(enviar_mensaje, inputs=[mensaje_input, usuario_input], outputs=respuesta_output)
        boton_limpiar.click(lambda: ("", "", ""), outputs=[mensaje_input, usuario_input, respuesta_output])
        boton_ver_tokens.click(ver_tokens, inputs=usuario_input, outputs=respuesta_output)

    interfaz.launch(server_port=config["puerto_ui"])


















