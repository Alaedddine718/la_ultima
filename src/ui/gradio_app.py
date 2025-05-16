import gradio as gr

from services.poll_service import PollService
from services.user_service import UserService
from services.nft_service import NFTService
from services.chatbot_service import ChatbotService

from repositories.encuesta_repo import EncuestaRepository
from repositories.usuario_repo import UsuarioRepository
from repositories.nft_repo import NFTRepository


# Servicios reales
poll_service = PollService(EncuestaRepository())
user_service = UserService(UsuarioRepository())
nft_service = NFTService(NFTRepository())
chatbot_service = ChatbotService(poll_service)

# Variable de sesión
sesion = {"usuario": None}

# LOGIN
def login(username, password):
    if user_service.login(username, password):
        sesion["usuario"] = username
        return f"✅ Bienvenido {username}"
    return "❌ Usuario o contraseña incorrectos"

# REGISTRO
def register(username, password):
    if user_service.register(username, password):
        return "✅ Usuario registrado correctamente"
    return "❌ El usuario ya existe"

# VOTAR
def votar(poll_id, opcion):
    if not sesion["usuario"]:
        return "❌ Debes iniciar sesión primero"
    try:
        resultado = poll_service.vote(poll_id, sesion["usuario"], opcion)
        return f"✅ Voto registrado: {resultado}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

# VER TOKENS
def ver_tokens():
    if not sesion["usuario"]:
        return ["❌ Debes iniciar sesión primero"]
    tokens = nft_service.obtener_tokens_usuario(sesion["usuario"])
    return [f"{t['token_id']} – {t['option']} ({t['poll_id']})" for t in tokens]

# CHATBOT
def responder_chat(mensaje):
    return chatbot_service.responder(sesion.get("usuario") or "anonimo", mensaje)

# UI
def lanzar_ui():
    with gr.Blocks() as demo:
        gr.Markdown("## 🎯 Plataforma de Votaciones en Vivo para Streamers")

        with gr.Tab("🔐 Iniciar Sesión"):
            user = gr.Textbox(label="Usuario")
            pwd = gr.Textbox(label="Contraseña", type="password")
            login_btn = gr.Button("Iniciar sesión")
            login_out = gr.Textbox(label="Estado")
            login_btn.click(fn=login, inputs=[user, pwd], outputs=login_out)

            gr.Markdown("### ¿No tienes cuenta?")
            new_user = gr.Textbox(label="Nuevo usuario")
            new_pwd = gr.Textbox(label="Nueva contraseña", type="password")
            reg_btn = gr.Button("Registrarse")
            reg_out = gr.Textbox()
            reg_btn.click(fn=register, inputs=[new_user, new_pwd], outputs=reg_out)

        with gr.Tab("🗳️ Encuestas"):
            poll_id = gr.Textbox(label="ID de la encuesta")
            opcion = gr.Textbox(label="Opción de voto")
            vote_btn = gr.Button("Votar")
            vote_out = gr.Textbox()
            vote_btn.click(fn=votar, inputs=[poll_id, opcion], outputs=vote_out)

        with gr.Tab("🪙 Mis Tokens"):
            token_btn = gr.Button("Ver mis tokens")
            token_out = gr.Textbox(lines=10)
            token_btn.click(fn=ver_tokens, outputs=token_out)

        with gr.Tab("🤖 Chatbot"):
            chat_in = gr.Textbox(label="Tu pregunta")
            chat_out = gr.Textbox(label="Respuesta del bot")
            chat_in.submit(fn=responder_chat, inputs=chat_in, outputs=chat_out)

    demo.launch()




