import gradio as gr

from src.services.poll_service import PollService
from src.services.user_service import UserService
from src.services.nft_service import NFTService
from src.services.chatbot_service import ChatbotService

from src.repositories.encuesta_repo import EncuestaRepository
from src.repositories.usuario_repo import UsuarioRepository
from src.repositories.nft_repo import NFTRepository

from src.controllers.ui_controller import UIController


def lanzar_ui():
    # Repositorios
    encuesta_repo = EncuestaRepository()
    usuario_repo = UsuarioRepository()
    nft_repo = NFTRepository()

    # Servicios
    poll_service = PollService(encuesta_repo)
    user_service = UserService(usuario_repo)
    nft_service = NFTService(nft_repo)
    chatbot_service = ChatbotService(poll_service)

    # Controlador
    ui_controller = UIController(poll_service, user_service, nft_service, chatbot_service)

    # Crear interfaz Gradio
    with gr.Blocks(title="La Última - Plataforma de Votaciones") as demo:
        gr.Markdown("# 📊 La Última - Plataforma de Votaciones en Vivo")

        with gr.Tab("Iniciar sesión"):
            username = gr.Textbox(label="Usuario")
            login_btn = gr.Button("Iniciar sesión")
            login_output = gr.Textbox(label="Resultado login")
            login_btn.click(fn=ui_controller.login, inputs=[username], outputs=[login_output])

        with gr.Tab("Crear Encuesta"):
            pregunta = gr.Textbox(label="Pregunta")
            opciones = gr.Textbox(label="Opciones (separadas por coma)")
            duracion = gr.Number(label="Duración en segundos", value=60)
            crear_btn = gr.Button("Crear encuesta")
            crear_output = gr.Textbox(label="Resultado")
            crear_btn.click(fn=ui_controller.crear_encuesta, inputs=[pregunta, opciones, duracion], outputs=[crear_output])

        with gr.Tab("Votar"):
            opcion = gr.Textbox(label="Tu voto")
            votar_btn = gr.Button("Votar")
            votar_output = gr.Textbox(label="Resultado")
            votar_btn.click(fn=ui_controller.votar_encuesta, inputs=[opcion], outputs=[votar_output])

        with gr.Tab("Ver Resultados"):
            resultados_btn = gr.Button("Ver resultados")
            resultados_output = gr.Textbox(label="Resultados")
            resultados_btn.click(fn=ui_controller.ver_resultados, inputs=[], outputs=[resultados_output])

        with gr.Tab("Chatbot"):
            chat_input = gr.Textbox(label="Mensaje")
            chat_btn = gr.Button("Enviar al chatbot")
            chat_output = gr.Textbox(label="Respuesta")
            chat_btn.click(fn=ui_controller.chatbot_responder, inputs=[chat_input], outputs=[chat_output])

    demo.launch()





