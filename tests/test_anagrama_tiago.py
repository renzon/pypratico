from exercicios.anagrama_tiago import eh_anagrama


def test_eh_anagrama_tiago():
    assert eh_anagrama('ABA', 'BAA')
    assert eh_anagrama('THE ALIAS MEN', 'ALAN SMITHEE')


def test_eh_anagrama_tiago_falso():
    assert not eh_anagrama('ABA', 'ACA')
