import gradio as gr

from src.services.poll_service import PollService
from src.services.user_service import UserService
from src.services.nft_service import NFTService
from src.services.chatbot_service import ChatbotService

from src.repositories.encuesta_repo import EncuestaRepository
from src.repositories.usuario_repo_factory import crear_usuario_repo
from src.repositories.nft_repo import NFTRepository

from src.controllers.ui_controller import UIController

# Inicialización de servicios y controlador
def lanzar_ui():
    encuesta_repo = EncuestaRepository()
    usuario_repo = crear_usuario_repo()
    nft_repo = NFTRepository()

    poll_service = PollService(encuesta_repo)
    user_service = UserService(usuario_repo)
    nft_service = NFTService(nft_repo)
    chatbot_service = ChatbotService(poll_service)

    ui_controller = UIController(poll_service, user_service, nft_service, chatbot_service)

    sesion = {"usuario": None, "token": None}

    def login(username, password):
        try:
            token = user_service.login(username, password)
            sesion["usuario"] = username
            sesion["token"] = token
            return f"Bienvenido {username}!"
        except Exception as e:
            return f"❌ {str(e)}"

    def registrar(username, password):
        try:
            user_service.registrar(username, password)
            return "✅ Usuario creado correctamente"
        except Exception as e:
            return f"❌ {str(e)}"

    def votar_ui(poll_id, opcion):
        if not sesion["usuario"]:
            return "Debes iniciar sesión."
        return ui_controller.votar_desde_ui(poll_id, sesion["usuario"], opcion)

    def ver_tokens():
        if not sesion["usuario"]:
            return "Inicia sesión para ver tus tokens."
        tokens = ui_controller.ver_tokens_usuario(sesion["usuario"])
        if not tokens:
            return "No tienes tokens."
        return "\n".join([f"ID: {t['token_id']} | Encuesta: {t['poll_id']} | Opción: {t['option']}" for t in tokens])

    def transferir(token_id, nuevo_owner):
        return ui_controller.transferir_token(token_id, nuevo_owner)

    def chatbot(mensaje):
        return ui_controller.responder_chat(sesion["usuario"] or "anonimo", mensaje)

    with gr.Blocks() as demo:
        gr.Markdown("# 🗳️ Plataforma de Votaciones en Vivo")

        with gr.Tab("🔐 Iniciar sesión / Registro"):
            gr.Markdown("### 🔑 Iniciar sesión")
            user = gr.Textbox(label="Nombre de usuario")
            pwd = gr.Textbox(label="Contraseña", type="password")
            login_btn = gr.Button("Iniciar sesión")
            login_out = gr.Textbox()
            login_btn.click(fn=login, inputs=[user, pwd], outputs=login_out)

            gr.Markdown("### 🆕 Crear cuenta")
            nuevo_user = gr.Textbox(label="Nuevo usuario")
            nueva_contra = gr.Textbox(label="Contraseña", type="password")
            registro_btn = gr.Button("Registrar usuario")
            registro_out = gr.Textbox()
            registro_btn.click(fn=registrar, inputs=[nuevo_user, nueva_contra], outputs=registro_out)

        with gr.Tab("🗳️ Votar"):
            poll_id = gr.Textbox(label="ID de la encuesta")
            opcion = gr.Textbox(label="Opción a votar")
            votar_btn = gr.Button("Votar")
            resultado_voto = gr.Textbox()
            votar_btn.click(fn=votar_ui, inputs=[poll_id, opcion], outputs=resultado_voto)

        with gr.Tab("🪙 Ver mis tokens"):
            tokens_btn = gr.Button("Mostrar tokens")
            tokens_out = gr.Textbox(lines=10)
            tokens_btn.click(fn=ver_tokens, outputs=tokens_out)

        with gr.Tab("🔄 Transferir token"):
            token_id = gr.Textbox(label="ID del token")
            nuevo_owner = gr.Textbox(label="Nuevo propietario")
            transferir_btn = gr.Button("Transferir")
            transferir_out = gr.Textbox()
            transferir_btn.click(fn=transferir, inputs=[token_id, nuevo_owner], outputs=transferir_out)

        with gr.Tab("🤖 Chatbot"):
            pregunta = gr.Textbox(label="Escribe tu mensaje")
            respuesta = gr.Textbox(label="Respuesta")
            pregunta.submit(fn=chatbot, inputs=pregunta, outputs=respuesta)

    demo.launch()











