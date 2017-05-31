import pytest

from pypraticot6.telefone import Telefone

NUMEROS_VALIDOS = ['8765432', 2345678]


def test_telefone_init():
    assert (Telefone() is not None)


@pytest.mark.parametrize('numero', NUMEROS_VALIDOS)
def test_ligar(numero):
    telefone = Telefone()
    assert 'ligar para ' + str(numero) == telefone.ligar(numero)


@pytest.mark.parametrize('numero', NUMEROS_VALIDOS)
def test_rediscar(numero):
    telefone = Telefone()
    telefone.ligar(numero)
    assert 'ligar para ' + str(numero) == telefone.rediscar()


@pytest.mark.parametrize('numero', NUMEROS_VALIDOS)
def test_rediscar_dois_telefone_diferentes(numero):
    telefone = Telefone()
    telefone.ligar(numero)
    telefone_2 = Telefone()
    outro_numero = str(numero) + '1'
    assert 'ligar para ' + str(outro_numero) == telefone_2.rediscar()
