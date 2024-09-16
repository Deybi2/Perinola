from clase_ronda import Ronda
from jugador.clase_jugador import Jugador 

jugador1 = Jugador("Tomas", 15)
jugador2 = Jugador("Andrés", 5)

ronda = Ronda()
ronda.agregarJugador(jugador1)
ronda.agregarJugador(jugador2)

print(ronda) 

ronda.pasarTurno()
print(f"Jugador en turno: {ronda.jugadorEnTurno()}") 