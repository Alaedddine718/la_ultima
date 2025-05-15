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
    def ver_tokens_usuario(self, username):
        return self.nft_service.obtener_tokens_usuario(username)

    def transferir_token(self, token_id, nuevo_owner):
        try:
            self.nft_service.transferir_token(token_id, nuevo_owner)
            return "Token transferido correctamente."
        except Exception as e:
            return str(e)

    def responder_chat(self, username, mensaje):
        return self.chatbot_service.responder(username, mensaje)

   
