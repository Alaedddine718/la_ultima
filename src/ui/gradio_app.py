import gradio as gr

from services.poll_service import PollService
from services.user_service import UserService
from services.nft_service import NFTService
from services.chatbot_service import ChatbotService

from repositories.encuesta_repo import EncuestaRepository
from repositories.usuario_repo import UsuarioRepository
from repositories.nft_repo import NFTRepository


# Crear servicios reales
poll_service = PollService(EncuestaRepository())
user_service = UserService(UsuarioRepository())
nft_service = NFTService(NFTRepository())
chatbot_service = ChatbotService(poll_service)

# Variables de sesión
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
        return "✅ Registro exitoso. Ya puedes iniciar sesión."
    return "❌ Ese nombre ya existe."

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
        return []
    tokens = nft_service.obtener_tokens_usuario(sesion["usuario"])
    return [f"{t['token_id']} – {t['option']} ({t['poll_id']})" for t in tokens]

# CHATBOT
def responder_chat(mensaje):
    return chatbot_service.responder(sesion.get("usuario") or "anonimo", mensaje)

# INTERFAZ
def lanzar_ui():
    with gr.Blocks() as demo:
        gr.Markdown("## 🎯 Plataforma de Votaciones para Streamers")
        with gr.Tab("🔐 Iniciar Sesión"):
            usuario = gr.Textbox(label="Usuario")
            contraseña = gr.Textbox(label="Contraseña", type="password")
            boton_login = gr.Button("Iniciar sesión")
            salida_login = gr.Textbox(label="Estado de sesión")
            boton_login.click(fn=login, inputs=[usuario, contraseña], outputs=salida_login)

            gr.Markdown("### ¿No tienes cuenta?")
            nuevo_user = gr.Textbox(label="Nuevo usuario")
            nueva_pass = gr.Textbox(label="Nueva contraseña", type="password")
            boton_registro = gr.Button("Registrarse")
            salida_registro = gr.Textbox()
            boton_registro.click(fn=register, inputs=[nuevo_user, nueva_pass], outputs=salida_registro)

        with gr.Tab("🗳️ Encuestas"):
            poll_id = gr.Textbox(label="ID de la encuesta")
            opcion = gr.Textbox(label="Tu opción de voto")
            boton_votar = gr.Button("Votar")
            salida_voto = gr.Textbox()
            boton_votar.click(fn=votar, inputs=[poll_id, opcion], outputs=salida_voto)

        with gr.Tab("🪙 Mis tokens"):
            boton_tokens = gr.Button("Ver tokens")
            salida_tokens = gr.Textbox(lines=10)
            boton_tokens.click(fn=ver_tokens, outputs=salida_tokens)

        with gr.Tab("🤖 Chatbot"):
            entrada = gr.Textbox(label="Haz una pregunta")
            salida = gr.Textbox(label="Respuesta")
            entrada.submit(fn=responder_chat, inputs=entrada, outputs=salida)

    demo.launch()


