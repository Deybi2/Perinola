import random

class Perinola:
    opciones = ["Pon 1", "Pon 2", "Toma 1", "Toma 2", "Todos Toman", "Ponen Todos"]

    def __init__(self):
        self.cara_visible = None 
    
    def tirar(self):
        self.cara_visible = random.choice(self.opciones)
        return self.cara_visible
    
    def __str__(self):
        return f"Salió: {self.cara_visible}" if self.cara_visible else "La perinola aún no ha sido lanzada."
