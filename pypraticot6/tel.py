from collections import namedtuple

from pypraticot6.telefone import Telefone

Usuario = namedtuple('Usuario', 'nome numero')


class Telefonista:
    """Telefonista mantém cadastro de usuários e pode ligar para eles"""

    def __init__(self):
        self.usuarios = []
        self.telefone = Telefone()

    def adicionar(self, nome, numero):
        self.usuarios.append(Usuario(nome, numero))

    def spam(self):
        for usuario in self.usuarios:
            ligacao = self.telefone.ligar(usuario.numero)
            yield f'Telefonista cadastro de {usuario.nome} {ligacao}'


if __name__ == '__main__':
    print(Usuario('Joao', '876543'))
