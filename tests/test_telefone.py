import pytest

from pypraticot6.telefone import Telefone


def test_telefone_init():
    assert (Telefone() is not None)


numeros_validos = ['8765432', 2345678]


@pytest.mark.parametrize('numero', numeros_validos)
def test_ligar(numero):
    telefone = Telefone()
    assert 'ligar para ' + str(numero) == telefone.ligar(numero)
