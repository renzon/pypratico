def buscar(*palavras_chave):
    """ Busca por caracteres que contenham a palavra chave em seu nome.
    Ex:
    
    >>> from exercicios.buscador import buscar
    >>> dict(buscar('BLACK', 'suit'))
    {'♠': 'BLACK SPADE SUIT', '♣': 'BLACK CLUB SUIT', '♥': 'BLACK HEART SUIT', '♦': 'BLACK DIAMOND SUIT'}
    >>> dict(buscar('BlAcK', 'suit', 'ClUb'))
    {'♣': 'BLACK CLUB SUIT'}
    >>> dict(buscar('chess', 'king'))
    {'♔': 'WHITE CHESS KING', '♚': 'BLACK CHESS KING'}
    
    :param palavras_chave: tupla de strings
    :return: generator onde cada elemento é uma tupla. O primeiro elemento da 
    tupla é o caracter e o segundo é seu nome. Assim ele pode ser utilizado no
    construtor de um dicionário
    """
