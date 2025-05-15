from transformers import pipeline

class ChatbotService:
    def __init__(self, poll_service):
        self.chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")
        self.poll_service = poll_service

    def responder(self, username, mensaje):
        msg = mensaje.lower()
        if "ganando" in msg or "quién va ganando" in msg:
            return "Consulta los resultados con el comando correspondiente."
        elif "cuánto falta" in msg:
            return "Depende de la duración de la encuesta. Puedes consultarlo en la sección de encuestas."
        else:
            return self.chatbot(mensaje)[0]["generated_text"]
