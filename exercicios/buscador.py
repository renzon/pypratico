import sys
import unicodedata


def buscar(*palavras_chave):
    """ Busca por caracteres que contenham a palavra chave em seu nome.
    Ex:

    >>> from exercicios.buscador import buscar
    >>> for caracter, nome in sorted(buscar('BLACK', 'suit')):
    ...     print(caracter, nome)
    ...
    ♠ BLACK SPADE SUIT
    ♣ BLACK CLUB SUIT
    ♥ BLACK HEART SUIT
    ♦ BLACK DIAMOND SUIT
    >>> for caracter, nome in sorted(buscar('suit')):
    ...     print(caracter, nome)
    ...
    ♠ BLACK SPADE SUIT
    ♡ WHITE HEART SUIT
    ♢ WHITE DIAMOND SUIT
    ♣ BLACK CLUB SUIT
    ♤ WHITE SPADE SUIT
    ♥ BLACK HEART SUIT
    ♦ BLACK DIAMOND SUIT
    ♧ WHITE CLUB SUIT
    🕴 MAN IN BUSINESS SUIT LEVITATING
    >>> dict(buscar('BlAcK', 'suit', 'ClUb'))
    {'♣': 'BLACK CLUB SUIT'}
    >>> for caracter, nome in sorted(buscar('chess', 'king')):
    ...     print(caracter, nome)
    ...
    ♔ WHITE CHESS KING
    ♚ BLACK CHESS KING

    :param palavras_chave: tupla de strings
    :return: generator onde cada elemento é uma tupla. O primeiro elemento da
    tupla é o caracter e o segundo é seu nome. Assim ele pode ser utilizado no
    construtor de um dicionário
    """
    limite = 0
    max_unicode_value = sys.maxunicode
    palavras_upper = [palavra.upper() for palavra in palavras_chave]
    while limite < max_unicode_value:
        caracter = chr(limite)
        try:
            unicode_name_upper = unicodedata.name(caracter).upper().split()
        except ValueError:
            pass
        else:
            if all(
                    palavra in unicode_name_upper
                    for palavra in palavras_upper
            ):
                yield (caracter, " ".join(unicode_name_upper))
        finally:
            limite += 1
