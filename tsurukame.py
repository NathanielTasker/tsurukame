from random import randrange as r

def random_legs():
    tsuru = r(100)
    kame = r(100)
    tsuru_legs = tsuru * 2
    kame_legs = kame * 4
    return [tsuru_legs + kame_legs, tsuru + kame]

def tsurukame(x):
    legs = x[0]
    creatures = x[1]
    all_tsuru = creatures * 2
    kame = round((legs - all_tsuru)/2)
    tsuru = round(creatures - kame)
    return [tsuru, kame]

r = random_legs()
print('%s legs, %s creatures are there.' % tuple(r))
print('%s tsuru, %s kame are there.' % tuple(tsurukame(r)))
