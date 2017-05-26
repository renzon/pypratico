from exercicios.anagrama_tiago import eh_anagrama


def test_eh_anagrama_tiago():
    assert eh_anagrama('ABA', 'BAA')


def test_eh_anagrama_tiago_falso():
    assert not eh_anagrama('ABA', 'ACA')
