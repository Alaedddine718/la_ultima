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
    nft_service = NFTService(nft_repo, config)
    chatbot_service = ChatbotService(config)

    ui_controller = UIController(poll_service, user_service, nft_service, chatbot_service)

    # Funciones para el chatbot
    def responder_chat(mensaje, username):
        try:
            respuesta = ui_controller.responder_chat(username, mensaje)
            return respuesta
        except Exception as e:
            return f"Error: {str(e)}"

    def ver_tokens(username):
        try:
            tokens = ui_controller.ver_tokens_usuario(username)
            if tokens:
                return "\n".join([str(token) for token in tokens])
            return "No tienes tokens."
        except Exception as e:
            return f"Error: {str(e)}"

    # Funciones de autenticación
    def registrarse(username, password):
        return ui_controller.registrar_usuario(username, password)

    def iniciar_sesion(username, password):
        return ui_controller.verificar_credenciales(username, password)

    # Interfaz Gradio
    with gr.Blocks() as demo:
        gr.Markdown("## Plataforma de Votaciones para Streamers")

        with gr.Tab("Chat"):
            with gr.Row():
                mensaje = gr.Textbox(label="Escribe un mensaje")
                usuario = gr.Textbox(label="Usuario")
            with gr.Row():
                salida = gr.Textbox(label="Respuesta del sistema")
                tokens_btn = gr.Button("Ver mis tokens")
            with gr.Row():
                btn_enviar = gr.Button("Enviar")
                btn_limpiar = gr.Button("Limpiar")

            btn_enviar.click(fn=responder_chat, inputs=[mensaje, usuario], outputs=salida)
            btn_limpiar.click(fn=lambda: "", inputs=None, outputs=salida)
            tokens_btn.click(fn=ver_tokens, inputs=usuario, outputs=salida)

        with gr.Tab("Autenticación"):
            gr.Markdown("### Registro e Inicio de sesión")
            usuario_reg = gr.Textbox(label="Usuario")
            password_reg = gr.Textbox(label="Contraseña", type="password")
            salida_auth = gr.Textbox(label="Resultado")
            btn_reg = gr.Button("Registrarse")
            btn_login = gr.Button("Iniciar sesión")

            btn_reg.click(fn=registrarse, inputs=[usuario_reg, password_reg], outputs=salida_auth)
            btn_login.click(fn=iniciar_sesion, inputs=[usuario_reg, password_reg], outputs=salida_auth)

    demo.launch(server_port=config["puerto_ui"])





















