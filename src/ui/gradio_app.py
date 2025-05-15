import gradio as gr

class GradioApp:
    def __init__(self, ui_controller):
        self.ui = ui_controller

    def interfaz_encuestas(self):
        def votar(poll_id, username, opcion):
            return self.ui.votar_desde_ui(poll_id, username, opcion)

        encuestas = self.ui.obtener_encuestas_activas()
        encuestas_info = "\n".join(
            f"{e.pregunta} (ID: {e.id}) - Opciones: {', '.join(e.opciones)}"
            for e in encuestas
        )

        with gr.Blocks() as demo:
            gr.Markdown("# Encuestas Activas")
            gr.Textbox(label="ID de encuesta", interactive=True)
            gr.Textbox(label="Tu nombre de usuario", interactive=True)
            gr.Textbox(label="Tu voto (opción)", interactive=True)
            gr.Textbox(value=encuestas_info, label="Encuestas", interactive=False)
            gr.Button("Votar").click(votar,
                                     inputs=["ID de encuesta", "Tu nombre de usuario", "Tu voto (opción)"],
                                     outputs=[])
        return demo

    def interfaz_chatbot(self):
        def responder(usuario, mensaje):
            return self.ui.responder_chat(usuario, mensaje)

        return gr.ChatInterface(fn=responder)

    def interfaz_tokens(self):
        def ver(username):
            tokens = self.ui.ver_tokens_usuario(username)
            return "\n".join([str(t) for t in tokens])

        def transferir(token_id, nuevo_owner):
            return self.ui.transferir_token(token_id, nuevo_owner)

        with gr.Blocks() as demo:
            gr.Markdown("# Galería de Tokens")
            gr.Textbox(label="Tu usuario", interactive=True)
            gr.Button("Ver mis tokens").click(ver, inputs=["Tu usuario"], outputs="text")
            gr.Textbox(label="Token ID", interactive=True)
            gr.Textbox(label="Nuevo propietario", interactive=True)
            gr.Button("Transferir token").click(transferir, inputs=["Token ID", "Nuevo propietario"], outputs="text")
        return demo

    def lanzar(self):
        with gr.TabbedInterface([
            self.interfaz_encuestas(),
            self.interfaz_chatbot(),
            self.interfaz_tokens()
        ], ["Encuestas", "Chatbot", "Tokens"]) as interfaz:
            interfaz.launch()
