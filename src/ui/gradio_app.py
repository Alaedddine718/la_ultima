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

    def crear_encuesta(pregunta, opciones_str, creador, duracion_str):
        try:
            opciones = [op.strip() for op in opciones_str.split(",")]
            duracion = int(duracion_str)
            encuesta_id = controller.crear_encuesta_ui(pregunta, opciones, creador, duracion)
            return f"Encuesta creada correctamente. ID: {encuesta_id}"
        except Exception as e:
            return f"Error al crear encuesta: {str(e)}"

    def votar_ui(encuesta_id, usuario, opcion):
        return controller.votar_desde_ui(encuesta_id, usuario, opcion)

    def ver_resultados_ui(encuesta_id):
        return controller.obtener_resultados_ui(encuesta_id)

    def ver_encuestas_activas_ui():
        return controller.obtener_encuestas_activas()

    def responder_chat_ui(username, mensaje):
        return controller.responder_chat(username, mensaje)

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
            duracion = gr.Textbox(label="Duración (en segundos)")
            resultado = gr.Textbox(label="Resultado")
            boton = gr.Button("Crear encuesta")
            boton.click(fn=crear_encuesta, inputs=[pregunta, opciones, creador, duracion], outputs=resultado)

        with gr.Tab("Votar"):
            encuesta_id = gr.Textbox(label="ID de la encuesta")
            usuario = gr.Textbox(label="Usuario")
            opcion = gr.Textbox(label="Opción")
            resultado_voto = gr.Textbox(label="Resultado del voto")
            boton_votar = gr.Button("Votar")
            boton_votar.click(fn=votar_ui, inputs=[encuesta_id, usuario, opcion], outputs=resultado_voto)

        with gr.Tab("Ver resultados"):
            encuesta_id_r = gr.Textbox(label="ID de la encuesta")
            resultados = gr.Textbox(label="Resultados")
            boton_ver = gr.Button("Ver resultados")
            boton_ver.click(fn=ver_resultados_ui, inputs=[encuesta_id_r], outputs=resultados)

        with gr.Tab("Encuestas activas"):
            activas_out = gr.Textbox(label="Encuestas activas")
            btn_activas = gr.Button("Mostrar encuestas activas")
            btn_activas.click(fn=ver_encuestas_activas_ui, outputs=activas_out)

        with gr.Tab("Chat"):
            user_chat = gr.Textbox(label="Usuario")
            mensaje_chat = gr.Textbox(label="Mensaje")
            respuesta_chat = gr.Textbox(label="Respuesta")
            btn_chat = gr.Button("Enviar mensaje")
            btn_chat.click(fn=responder_chat_ui, inputs=[user_chat, mensaje_chat], outputs=respuesta_chat)

    demo.launch()






























