from pypraticot6.telefonista import Telefonista


def test_telefonista_init():
    """Telefonista possui inicializador vazio"""
    assert Telefonista()


def telefonista():
    telefonista = Telefonista()
    telefonista.adicionar('Renzo', '2345678')
    telefonista.adicionar('Tiago', '8765432')
    return telefonista


def teste_adicionar_usuario():
    """Usuário pode ser adicionado com seu telefone"""
    assert [('Renzo', '2345678'),
            ('Tiago', '8765432')] == telefonista().usuarios


def test_spam():
    ligacoes_para_usuarios = list(telefonista().spam())
    ligacoes_esperadas = [
        'Telefonista cadastro de Renzo ligar para 2345678',
        'Telefonista cadastro de Tiago ligar para 8765432',
    ]
    assert ligacoes_esperadas == ligacoes_para_usuarios
