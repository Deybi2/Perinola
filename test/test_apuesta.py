import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'apuesta')))
from clase_apuesta import Apuesta
import pytest

def test_inicializar_apuesta():
    apuesta = Apuesta()
    assert apuesta.fichas == 0

def test_poner_fichas():
    apuesta = Apuesta()
    apuesta.ponerFicha(3)
    assert apuesta.fichas == 3

def test_tomar_fichas():
    apuesta = Apuesta()
    apuesta.ponerFicha(5)
    apuesta.tomarFicha(2)
    assert apuesta.fichas == 3

def test_tomar_todas_fichas():
    apuesta = Apuesta()
    apuesta.ponerFicha(5)
    assert apuesta.tomarTodas() == 5
    assert apuesta.fichas == 0

def test_tiene_fichas():
    apuesta = Apuesta()
    apuesta.ponerFicha(3)
    assert apuesta.tieneFicha(2) == True

def test_esta_vacia():
    apuesta = Apuesta()
    assert apuesta.estaVacia() == True
    apuesta.ponerFicha(1)
    assert apuesta.estaVacia() == False