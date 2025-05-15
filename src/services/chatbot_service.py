from transformers import pipeline

class ChatbotService:
    def __init__(self, poll_service):
        self.chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")
        self.poll_service = poll_service

    
