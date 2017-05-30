# -*- coding: utf-8 -*-

"""

Regras do fizzbuzz

1.Se a posição for multiplo de 3: fizz.
2.Se a posição for multiplo de 5: buzz.
3.Se a posição for multiplo de 3 e  5: fizzbuzz.
4.Se for qualquer outra posição fale o próprio número.

"""
def robot(pas):
    if pas == 4:
        return str(4)
    if pas == 2:
        return '2'
    return '1'

if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'
