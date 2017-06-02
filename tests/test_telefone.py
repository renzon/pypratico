import pytest

from pypraticot6.telefone import Telefone, RediscarExcecao

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
    outro_telefone = Telefone()
    outro_numero = str(numero) + '1'
    outro_telefone.ligar(outro_numero)
    assert 'ligar para ' + str(numero) == telefone.rediscar()
    assert 'ligar para ' + str(outro_numero) == outro_telefone.rediscar()


def test_rediscar_excecao():
    """Certifica que tentar rediscar ante de fazer uma ligacao lança exceção"""
    telefone = Telefone()
    with pytest.raises(RediscarExcecao):
        telefone.rediscar()
