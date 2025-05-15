class UIController:
    def __init__(self, poll_service, user_service, nft_service, chatbot_service):
        self.poll_service = poll_service
        self.user_service = user_service
        self.nft_service = nft_service
        self.chatbot_service = chatbot_service

    def obtener_encuestas_activas(self):
        return list(self.poll_service.encuestas_activas.values())

    def votar_desde_ui(self, poll_id, username, opcion):
        try:
            self.poll_service.votar(poll_id, username, opcion)
            self.nft_service.generar_token(username, poll_id, opcion)
            return "Voto registrado y token generado."
        except Exception as e:
            return str(e)

   
