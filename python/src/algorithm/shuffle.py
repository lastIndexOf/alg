from random import randint


def shuffle(l):
    ret = [*l]
    length = len(ret)

    while length > 0:
        randi = randint(0, length - 1)
        ret[length-1], ret[randi] = ret[randi], ret[length-1]
        length -= 1

    return ret


l = [x for x in range(10)]
print(l)
print(shuffle(l))