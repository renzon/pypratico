import requests


def avatar(usuario):
    """Retorna o link com avatar do usuário

    :param usuario: str com nome do usuario
    :return: str
    """

    reposta = requests.get(f'https://api.github.com/users/{usuario}')
    return reposta.json()['avatar_url']


if __name__ == '__main__':
    print(avatar('renzon'))
