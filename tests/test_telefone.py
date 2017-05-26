from pypraticot6.telefone import Telefone


def test_telefone_init():
    assert (Telefone() is not None)


def test_ligar_com_string():
    telefone = Telefone()
    assert 'ligar para 2345678' == telefone.ligar('2345678')


def test_ligar_com_int():
    telefone = Telefone()
    assert 'ligar para 2345678' == telefone.ligar(2345678)
