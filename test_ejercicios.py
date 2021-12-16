import pytest

from examen import *
from ejercicios import *

lista_filtrada = [{"denominacion": "No hay respiro", "descripcion": "Buscamos llegar a tres pases en el equipo para devolver el balón al sacador de banda = 2 ptos.\nEste devolverá el balón al equipo pasador = 1 pto.\n(2x2, 3x3, 4x4...+1)\nVariante: logrados 3 pases en el equipo al pasar al sacador intercambio de funciones.", "estrategia": ["Siempre en movimiento.", "Acción para el otro.", "Dos actitudes en defensa a descubrir ante diversas valoraciones en el jugar.", "Enriquecer con cortes y su defensa. Chocar los cortes."], "duracion": 20}, {"denominacion": "Mensaje", "descripcion": "Intentamos pasar el balón a un jugador defendido dentro del círculo.\nSuperioridad atacante.", "estrategia": ["Desmarcarse y buscar línea de pase.", "Sellar el apoyo fuerte del defensor.", "Fijar al defensor y dar referencia."], "duracion": 10}]


def test_filtra_ejercicios():
    assert filtra_ejercicios(lista_filtrada, 10) == [{"denominacion": "Mensaje", "descripcion": "Intentamos pasar el balón a un jugador defendido dentro del círculo.\nSuperioridad atacante.", "estrategia": ["Desmarcarse y buscar línea de pase.", "Sellar el apoyo fuerte del defensor.", "Fijar al defensor y dar referencia."], "duracion": 10}]


def test_duracion():
    assert duracion_ejercicios(ejercicios) == 490
    

def test_entrenamiento():
    resultado = entrenamiento(ejercicios, 30)
    sumaminutos = 0
    for ejercicio in resultado:
        sumaminutos += ejercicio["duracion"]
    assert sumaminutos == 30
