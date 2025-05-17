class ChatbotService:
    def __init__(self, poll_service):
        self.poll_service = poll_service
        self.respuestas = {
            "hola": "¡Hola! ¿En qué puedo ayudarte?",
            "cómo estás": "Estoy bien, gracias.",
            "adiós": "¡Hasta luego!",
            "encuesta": "Puedes crear o participar en encuestas en la interfaz.",
            "gracias": "De nada, ¡para eso estoy!"
        }

    def responder(self, username, mensaje):
        mensaje = mensaje.lower()
        for clave in self.respuestas:
            if clave in mensaje:
                return f"{username}, {self.respuestas[clave]}"
        return f"{username}, no entendí tu mensaje."

