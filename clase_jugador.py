class Jugador:
    def __init__(self, nombre, fichas=5):
        self.nombre = nombre
        self.fichas = fichas

    def darFicha(self, cuantas=1):
        self.fichas += cuantas

    def sacarFicha(self, cuantas=1):
        if cuantas > self.fichas:
            raise ValueError(f"{self.nombre} no tiene suficientes fichas.")
        self.fichas -= cuantas

    def tieneFicha(self, cuantas=1):
        return self.fichas >= cuantas

    def sinFichas(self):
        return self.fichas == 0

    def __str__(self):
        return f"{self.nombre}, {self.fichas} ficha(s)"
