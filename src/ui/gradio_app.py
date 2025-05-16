import gradio as gr

def lanzar_ui():
    def saludar(nombre):
        return f"¡Hola, {nombre}! Bienvenido al stream."

    interfaz = gr.Interface(
        fn=saludar,
        inputs="text",
        outputs="text",
        title="Votaciones en Vivo",
        description="Escribe tu nombre para saludar.",
    )

    interfaz.launch()



