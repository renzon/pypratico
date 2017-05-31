from exercicios.palindromo import eh_palindromo


def test_palindromo_vazio():
    assert eh_palindromo('')


def test_palindromo_um_caracter():
    assert eh_palindromo('a')


def test_nao_eh_palindromo():
    assert not eh_palindromo('ab')
