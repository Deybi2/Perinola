class Ronda:
    def __init__(self):
        self.jugadores = []

    def agregarJugador(self, jugador):
        if jugador.sinFichas():
            raise ValueError(f"{jugador.nombre} no tiene fichas, no puede unirse a la ronda.")
        self.jugadores.append(jugador)

    def sacarJugadoresSinFichas(self):
        self.jugadores = [jugador for jugador in self.jugadores if not jugador.sinFichas()]

    def jugadorEnTurno(self):
        if not self.jugadores:
            return None
        return self.jugadores[0]

    def pasarTurno(self):
        if self.jugadores:
            jugador_actual = self.jugadores.pop(0)
            self.jugadores.append(jugador_actual)

    def quedaUnSoloJugador(self):
        return len(self.jugadores) == 1

    def __str__(self):
        return '\n'.join([str(jugador) for jugador in self.jugadores])
