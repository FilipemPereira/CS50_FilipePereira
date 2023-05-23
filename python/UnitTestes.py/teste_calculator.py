from calculator import square

def teste_square2():
    assert square(2) == 4
    assert square(3) == 9
    assert square(0) == 0
    assert square(-2) == 4
    assert square(-3) == 9

def test_str():
    with pytest.raises(TypeError):
        square("cat")