import gradio as gr

# Función simulada para responder preguntas del usuario
def responder_chat(mensaje):
    if "ganando" in mensaje.lower():
        return "Todavía no hay resultados disponibles."
    else:
        return "Soy un chatbot simulado. Pregunta algo sobre el stream."

# Función simulada para votar
def votar_encuesta(nombre, opcion):
    return f"{nombre} ha votado por '{opcion}' ✅"

def lanzar_ui():
    with gr.Blocks() as demo:
        gr.Markdown("## 🎯 Plataforma de Votaciones en Vivo para Streamers")
        gr.Markdown("Participa en encuestas, habla con el chatbot y gana tokens NFT simulados.")

        with gr.Tab("Encuestas"):
            nombre = gr.Textbox(label="Tu nombre de usuario")
            opcion = gr.Radio(["Opción A", "Opción B"], label="¿Qué prefieres?")
            boton_votar = gr.Button("Votar")
            salida_voto = gr.Textbox(label="Resultado del voto")

            boton_votar.click(fn=votar_encuesta, inputs=[nombre, opcion], outputs=salida_voto)

        with gr.Tab("Chatbot"):
            entrada_chat = gr.Textbox(label="Haz una pregunta")
            salida_chat = gr.Textbox(label="Respuesta del bot")
            entrada_chat.submit(responder_chat, inputs=entrada_chat, outputs=salida_chat)

    demo.launch()

