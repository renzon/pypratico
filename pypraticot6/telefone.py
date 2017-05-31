class RediscarExcecao(Exception):
    pass


class Telefone:
    def __init__(self):
        self.ultimo_numero = None

    def ligar(self, numero):
        self.ultimo_numero = numero
        return f'ligar para {numero}'

    def rediscar(self):
        # if self.ultimo_numero is None:
        #     raise RediscarExcecao()
        return self.ligar(self.ultimo_numero)
