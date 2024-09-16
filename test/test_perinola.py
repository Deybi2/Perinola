import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'perinola')))
from clase_perinola import Perinola
import pytest

def test_inicializar_perinola():
    perinola = Perinola()
    assert perinola.cara_visible in Perinola.opciones

def test_tirar_perinola():
    perinola = Perinola()
    resultado = perinola.tirar()
    assert resultado in Perinola.opciones
    assert perinola.cara_visible == resultado