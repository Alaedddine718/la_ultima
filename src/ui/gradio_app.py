import gradio as gr
import json
from src.services.poll_service import PollService
from src.services.user_service import UserService
from src.services.nft_service import NFTService
from src.services.chatbot_service import ChatbotService
from src.repositories.encuesta_repo import crear_encuesta_repo
from src.repositories.usuario_repo import crear_usuario_repo
from src.repositories.nft_repo import crear_nft_repo
from src.controllers.ui_controller import UIController
from src.config import cargar_config

config = cargar_config()

def lanzar_ui():
    encuesta_repo = crear_encuesta_repo()
    usuario_repo = crear_usuario_repo()
    nft_repo = crear_nft_repo()

    poll_service = PollService(encuesta_repo)
    user_service = UserService(usuario_repo)
    nft_service = NFTService(nft_repo, config)
    chatbot_service = ChatbotService(config.get("modelo_chatbot", "default"))

    controller = UIController(poll_service, user_service, nft_service, chatbot_service)

    def manejar_registro(username, password):
        return controller.registrar_usuario(username, password)

    def manejar_login(username, password):
        return controller.iniciar_sesion(username, password)

    def crear_encuesta_fn(pregunta, opciones, creador, duracion):
        lista_opciones = [op.strip() for op in opciones.split(",")]
        return controller.crear_encuesta(pregunta, lista_opciones, creador, duracion)

    with gr.Blocks() as demo:
        gr.Markdown("# Bienvenido a la app")

        with gr.Tab("Registrarse"):
            user_r = gr.Textbox(label="Usuario")
            pass_r = gr.Textbox(label="Contraseña", type="password")
            out_r = gr.Textbox(label="Resultado del registro")
            btn_r = gr.Button("Registrarse")
            btn_r.click(fn=manejar_registro, inputs=[user_r, pass_r], outputs=out_r)

        with gr.Tab("Iniciar sesión"):
            user_l = gr.Textbox(label="Usuario")
            pass_l = gr.Textbox(label="Contraseña", type="password")
            out_l = gr.Textbox(label="Resultado del login")
            btn_l = gr.Button("Iniciar sesión")
            btn_l.click(fn=manejar_login, inputs=[user_l, pass_l], outputs=out_l)

        with gr.Tab("Crear encuesta"):
            pregunta = gr.Textbox(label="Pregunta")
            opciones = gr.Textbox(label="Opciones (separadas por coma)")
            creador = gr.Textbox(label="Creador")
            duracion = gr.Number(label="Duración (en segundos)", value=60)
            out_encuesta = gr.Textbox(label="Resultado")
            crear_btn = gr.Button("Crear encuesta")
            crear_btn.click(
                fn=crear_encuesta_fn,
                inputs=[pregunta, opciones, creador, duracion],
                outputs=out_encuesta
            )

    demo.launch()





























