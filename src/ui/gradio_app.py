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
    nft_service = NFTService(nft_repo)
    chatbot_service = ChatbotService(config["modelo_chatbot"])

    ui_controller = UIController(poll_service, user_service, nft_service, chatbot_service)

    def registrar_usuario(username, password):
        try:
            user_service.registrar(username, password)
            return "Usuario registrado correctamente."
        except Exception as e:
            return str(e)

    def login_usuario(username, password):
        try:
            token = user_service.login(username, password)
            return f"Sesión iniciada. Token: {token}"
        except Exception as e:
            return str(e)

    def responder_chat(mensaje, username):
        if not mensaje or not username:
            return "Por favor, escribe un mensaje y tu usuario."
        return ui_controller.responder_chat(username, mensaje)

    def ver_tokens_usuario(username):
        tokens = ui_controller.ver_tokens_usuario(username)
        return "\n".join([str(t) for t in tokens]) if tokens else "No tienes tokens."

    with gr.Blocks(title="Plataforma de Votaciones para Streamers") as demo:
        gr.Markdown("# Plataforma de Votaciones para Streamers")

        with gr.Tab("Chat"):
            with gr.Row():
                mensaje = gr.Textbox(label="Escribe un mensaje")
                username = gr.Textbox(label="Usuario")
            with gr.Row():
                enviar_btn = gr.Button("Enviar")
                limpiar_btn = gr.Button("Limpiar")
            respuesta = gr.Textbox(label="Respuesta del sistema", interactive=False)
            ver_tokens_btn = gr.Button("Ver mis tokens")

        with gr.Tab("Autenticación"):
            gr.Markdown("## Registro e Inicio de sesión")
            user = gr.Textbox(label="Usuario")
            pwd = gr.Textbox(label="Contraseña", type="password")
            with gr.Row():
                btn_reg = gr.Button("Registrarse")
                btn_login = gr.Button("Iniciar sesión")
            auth_output = gr.Textbox(label="Resultado")

        enviar_btn.click(fn=responder_chat, inputs=[mensaje, username], outputs=respuesta)
        limpiar_btn.click(fn=lambda: ("", "", ""), outputs=[mensaje, username, respuesta])
        ver_tokens_btn.click(fn=ver_tokens_usuario, inputs=username, outputs=respuesta)

        btn_reg.click(fn=registrar_usuario, inputs=[user, pwd], outputs=auth_output)
        btn_login.click(fn=login_usuario, inputs=[user, pwd], outputs=auth_output)

    demo.launch(server_port=config["puerto_ui"])




















