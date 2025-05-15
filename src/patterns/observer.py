class Observable:
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def notificar_observadores(self, evento):
        for obs in self.observadores:
            obs.update(evento)

class Observador:
    def update(self, evento):
        pass  # implementar en cada clase que escuche
