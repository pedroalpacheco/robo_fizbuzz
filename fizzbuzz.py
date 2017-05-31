# -*- coding: utf-8 -*-

"""

Regras do fizzbuzz

1.Se a posição for multiplo de 3: fizz.
2.Se a posição for multiplo de 5: buzz.
3.Se a posição for multiplo de 3 e  5: fizzbuzz.
4.Se for qualquer outra posição fale o próprio número.

parei video 8:42

"""
from functools import partial


multiple_of = lambda base, num: num % base == 0
multiple_of_5 = partial(multiple_of,5)
multiple_of_3 = partial(multiple_of,3)



def robot(pos):
    say = str(pos)

    if multiple_of_3(pos) or multiple_of_5(pos):
        say = 'fizzbuzz'

    elif multiple_of_5(pos):
        say = 'buzz'

    elif multiple_of_3(pos):
        say = 'fizz'

    return say

def assert_equal(first, second, line):
    try:
        assert first == second
    except AssertionError:
        print('Line', line, first, second)

if __name__ == '__main__':
    assert_equal(robot(1) , '1', '43')
    assert_equal(robot(2) , '2', '44')
    assert_equal(robot(4) , '4', '45')
                          
    assert_equal(robot(3) , 'fizz', '47')
    assert_equal(robot(6) , 'fizz', '48')
    assert_equal(robot(9) , 'fizz', '49')

    assert_equal(robot(5) , 'buzz', '51')
    assert_equal(robot(10) , 'buzz', '52')
    assert_equal(robot(20) , 'buzz', '53')
                           
    assert_equal(robot(15) , 'fizzbuzz', '55')
    assert_equal(robot(30) , 'fizzbuzz', '56')
    assert_equal(robot(45) , 'fizzbuzz', '57')
