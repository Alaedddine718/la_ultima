import random

class DesempateStrategy:
    def resolver(self, opciones_con_empate):
        raise NotImplementedError()

class EstrategiaAlfabetica(DesempateStrategy):
    def resolver(self, opciones_con_empate):
        return sorted(opciones_con_empate)[0]


