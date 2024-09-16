import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'jugador')))
from clase_jugador import Jugador
import pytest

def test_inicializar_jugador():
    jugador = Jugador("Tomas", 10)
    assert jugador.nombre == "Tomas"
    assert jugador.fichas == 10

def test_dar_fichas():
    jugador = Jugador("Andres")
    jugador.darFicha(5)
    assert jugador.fichas == 10

def test_sacar_fichas():
    jugador = Jugador("Andres", 10)
    jugador.sacarFicha(3)
    assert jugador.fichas == 7

def test_sin_fichas():
    jugador = Jugador("Andres", 0)
    assert jugador.sinFichas() == True