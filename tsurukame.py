from random import randrange as r

def random_legs():
    tsuru_legs = r(100) * 2
    kame_legs = r(100) * 4
    return tsuru_legs + kame_legs

print('%s legs are there.' % random_legs())
