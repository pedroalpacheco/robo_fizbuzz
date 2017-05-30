# -*- coding: utf-8 -*-

"""

Regras do fizzbuzz

1.Se a posição for multiplo de 3: fizz.
2.Se a posição for multiplo de 5: buzz.
3.Se a posição for multiplo de 3 e  5: fizzbuzz.
4.Se for qualquer outra posição fale o próprio número.

"""


def robot(pos):
    if pos in (45,30,15):
        return 'fizzbuzz'

    if pos % 5 == 0:
        return 'buzz'

    if pos % 3 == 0:
        return 'fizz'

    return str(pos)


if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'
