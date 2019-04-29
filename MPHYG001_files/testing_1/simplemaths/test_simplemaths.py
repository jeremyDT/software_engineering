import pytest
from simplemaths.simplemaths import SimpleMaths as sm

# class TestSimpleMaths():


def test_init_pos():
    for i in range(0, 100, 10):
        sm(i)


def test_init_neg():
    with pytest.raises(TypeError):
        sm(1.0)
    with pytest.raises(TypeError):
        sm("wrong_string")


def test_square():
    obj = sm(5)
    assert obj.square() == 25
    assert obj.factorial() == 120


def test_power():
    obj = sm(10)
    assert obj.power(4) == 10000


def test_odd_even():

    assert sm(10).odd_or_even() == "Even"
    assert sm(373873).odd_or_even() == "Odd"
    assert sm(0).odd_or_even() == "Even"


def test_sqrt():
    assert sm(100).square_root() == 10
    assert sm(10).square_root() == pytest.approx(3.162277, rel=0.1, abs=0.1)
