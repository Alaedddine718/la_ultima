from abc import ABC, abstractmethod

class EncuestaRepository(ABC):
    @abstractmethod
    def guardar_encuesta(self, encuesta_dict):
        pass

    @abstractmethod
    def obtener_encuesta(self, encuesta_id):
        pass

