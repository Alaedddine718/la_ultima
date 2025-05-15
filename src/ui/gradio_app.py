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

       