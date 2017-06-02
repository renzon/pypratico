from unittest.mock import Mock

import pytest

from pypraticot6 import tel


def test_telefonista_init():
    """Telefonista possui inicializador vazio"""
    assert tel.Telefonista()


@pytest.fixture(scope='module')
def telefonista():
    telefonista_ = tel.Telefonista()
    telefonista_.adicionar('Renzo', '2345678')
    telefonista_.adicionar('Tiago', '8765432')
    return telefonista_


@pytest.fixture
def telefonista_fake(telefonista):
    # setup
    telefone_orinal = telefonista.telefone
    telefone_mock = Mock()
    telefone_mock.ligar.side_effect = (lambda numero:
                                       f'ligar de mentira para {numero}')
    telefonista.telefone = telefone_mock

    yield telefonista

    # tear down
    telefonista.telefone = telefone_orinal


def teste_adicionar_usuario(telefonista):
    """Usuário pode ser adicionado com seu telefone"""
    assert [('Renzo', '2345678'),
            ('Tiago', '8765432')] == telefonista.usuarios


def test_spam_unitario(telefonista_fake):
    ligacoes_para_usuarios = list(telefonista_fake.spam())
    ligacoes_esperadas = [
        'Telefonista cadastro de Renzo ligar de mentira para 2345678',
        'Telefonista cadastro de Tiago ligar de mentira para 8765432',
    ]
    assert ligacoes_esperadas == ligacoes_para_usuarios
    telefonista_fake.telefone.ligar.assert_any_call('2345678')
    telefonista_fake.telefone.ligar.assert_any_call('8765432')


# Test de integração

def test_spam_integracao(telefonista):
    ligacoes_para_usuarios = list(telefonista.spam())
    ligacoes_esperadas = [
        'Telefonista cadastro de Renzo ligar para 2345678',
        'Telefonista cadastro de Tiago ligar para 8765432',
    ]
    assert ligacoes_esperadas == ligacoes_para_usuarios
