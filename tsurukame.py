from random import randrange as r

def random_legs():
    tsuru = r(100) * 2
    kame = r(100) * 4
    tsuru_legs = tsuru * 2
    kame_legs = kame * 4
    return (tsuru + kame, tsuru_legs + kame_legs)

print('%s legs, %s creatures are there.' % random_legs())
