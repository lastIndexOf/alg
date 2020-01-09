from random import randint

l = {x: randint(60, 100) for x in range(10)}

print(dict(sorted(l.items(), key=lambda t: t[1], reverse=True)))