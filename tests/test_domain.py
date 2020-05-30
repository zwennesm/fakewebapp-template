from application.calc import Calc


def test_add_two_numbers():
    c = Calc()
    res = c.add(4, 5)

    assert res == 9


def test_add_three_numbers():
    c = Calc()
    res = c.add(4, 5, 11)

    assert res == 20
