import pytest

from pypraticot6 import tel


def test_telefonista_init():
    """Telefonista possui inicializador vazio"""
    assert tel.Telefonista()


class TelefoneMock:
    def __init__(self):
        self.numeros = []

    def ligar(self, numero):
        self.numeros.append(numero)
        return f'ligar de mentira para {numero}'


@pytest.fixture(scope='module')
def telefonista():
    telefonista_ = tel.Telefonista()
    telefonista_.adicionar('Renzo', '2345678')
    telefonista_.adicionar('Tiago', '8765432')
    return telefonista_


@pytest.fixture
def telefonista_fake(telefonista):
    # setup
    telefone_orinal=telefonista.telefone
    telefonista.telefone = TelefoneMock()
    yield telefonista

    #tear down
    telefonista.telefone=telefone_orinal





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
    assert ['2345678', '8765432'] == telefonista_fake.telefone.numeros


# Test de integração

def test_spam_integracao(telefonista):
    ligacoes_para_usuarios = list(telefonista.spam())
    ligacoes_esperadas = [
        'Telefonista cadastro de Renzo ligar para 2345678',
        'Telefonista cadastro de Tiago ligar para 8765432',
    ]
    assert ligacoes_esperadas == ligacoes_para_usuarios
