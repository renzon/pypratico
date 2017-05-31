ultimo_numero = None


class Telefone:
    def ligar(self, numero):
        global ultimo_numero
        ultimo_numero = numero
        return f'ligar para {numero}'

    def rediscar(self):
        return self.ligar(ultimo_numero)
