import sys

from z3 import *
import pandas as pd


def solve(input_data):
    s = Solver()

    ### Dictionaries ###

    clothDic = {
        'shirt': Bool('shirt'),
        'pullover': Bool('pullover'),
        'jacket': Bool('jacket'),
        'trousers': Bool('trousers'),
        'skirt': Bool('skirt'),
        'shoes': Bool('shoes'),
        'flipFlops': Bool('flipFlops'),
        'hat': Bool('hat'),
        'sunglasses': Bool('sunglasses')
    }

    colorsDic = {
        'white': Bool('white'),
        'black': Bool('black'),
        'blue': Bool('blue'),
        'pink': Bool('pink'),
        'brown': Bool('brown'),
        'green': Bool('green'),
        'yellow': Bool('yellow'),
        'red': Bool('red'),
        'orange': Bool('orange')
    }

    ### Constraints ###

    # Clothes #

    s.add(Not(And(clothDic['skirt'], clothDic['trousers'])))
    s.add(Not(And(clothDic['shoes'], clothDic['flipFlops'])))
    s.add(Not(And(clothDic['pullover'], clothDic['jacket'])))
    s.add(Not(And(clothDic['pullover'], clothDic['flipFlops'])))

    s.add(Implies(clothDic['pullover'], clothDic['shirt']))
    s.add(Implies(clothDic['jacket'], clothDic['shirt']))
    s.add(Implies(clothDic['jacket'], Or(clothDic['shirt'], clothDic['trousers'])))
    s.add(Implies(And(clothDic['flipFlops'], clothDic['sunglasses']), clothDic['hat']))

    # Colors #

    s.add(Not(And(colorsDic['red'], colorsDic['orange'])))
    s.add(Not(And(colorsDic['pink'], colorsDic['red'])))
    s.add(Not(And(colorsDic['blue'], colorsDic['green'])))
    s.add(Not(And(colorsDic['brown'], colorsDic['pink'])))
    s.add(Not(And(colorsDic['pink'], colorsDic['green'])))
    s.add(Not(And(colorsDic['green'], colorsDic['yellow'])))
    s.add(Not(And(colorsDic['blue'], colorsDic['yellow'])))
    s.add(Not(And(colorsDic['red'], colorsDic['green'])))
    s.add(Not(And(colorsDic['brown'], colorsDic['black'])))

    data = list(input_data.itertuples(index=False))

    for cloth, color in data:
        print(cloth, color)
        s.add(And(clothDic[cloth], colorsDic[color]))

    for constraint in s.assertions():
        print(constraint)

    if s.check() == sat:
        print("Sat")
    else:
        print('Unsat')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        # TODO: print error
        exit()

    input_data = pd.read_csv(sys.argv[1], delimiter=' ')
    solve(input_data)
