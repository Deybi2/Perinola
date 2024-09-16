import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ronda')))
from clase_ronda import Ronda
from clase_jugador import Jugador
import pytest

def test_agregar_jugador():
    ronda = Ronda()
    jugador = Jugador("Tomas", 5)
    ronda.agregarJugador(jugador)
    assert len(ronda.jugadores) == 1

def test_jugador_en_turno():
    ronda = Ronda()
    jugador = Jugador("Tomas", 5)
    ronda.agregarJugador(jugador)
    assert ronda.jugadorEnTurno() == jugador

def test_pasar_turno():
    ronda = Ronda()
    jugador1 = Jugador("Tomas", 5)
    jugador2 = Jugador("Andres", 5)
    ronda.agregarJugador(jugador1)
    ronda.agregarJugador(jugador2)
    ronda.pasarTurno()
    assert ronda.jugadorEnTurno() == jugador2

def test_sacar_jugadores_sin_fichas():
    ronda = Ronda()
    jugador1 = Jugador("Tomas", 0)
    jugador2 = Jugador("Andres", 5)
    ronda.agregarJugador(jugador1)
    ronda.agregarJugador(jugador2)
    ronda.sacarJugadoresSinFichas()
    assert len(ronda.jugadores) == 1
    assert ronda.jugadores[0] == jugador2

def test_queda_un_solo_jugador():
    ronda = Ronda()
    jugador = Jugador("Tomas", 5)
    ronda.agregarJugador(jugador)
    assert ronda.quedaUnSoloJugador() == True