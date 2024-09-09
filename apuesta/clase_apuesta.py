class Apuesta:
    def __init__(self):
        self.fichas = 0 
    
    def ponerFicha(self, cuantas=1):
        self.fichas += cuantas
    
    def tomarFicha(self, cuantas=1):
        if cuantas > self.fichas:
            raise ValueError("No hay suficientes fichas en la apuesta.")
        self.fichas -= cuantas

    def tomarTodas(self):
        fichas_tomadas = self.fichas
        self.fichas = 0
        return fichas_tomadas

    def tieneFicha(self, cuantas=1):
        return self.fichas >= cuantas

    def estaVacia(self):
        return self.fichas == 0

    def __str__(self):
        return f"Apuesta: {self.fichas} ficha(s)"
