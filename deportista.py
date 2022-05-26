from persona import Persona


class Deportista(Persona):
    def __init__(self, nombre, edad, altura, sexo, deporte, anos):
        super().__init__(nombre, edad, altura, sexo)
        self._deporte = deporte
        self._anosPracticando = anos

    def getDeporte(self):
        return self._deporte

    def getAnosPracticando(self):
        return self._anosPracticando

    def setDeporte(self, nuevo):
        self._deporte = nuevo

    def setAnosPracticando(self, anos):
        self._anosPracticando = anos
