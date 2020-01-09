def sum_reverse_sort(l: list):
    ret = 0

    for i in range(len(l)):
        st = l[i]
        for t in range(i+1, len(l)):
            if st > l[t]:
                ret += 1

    return ret


def sum_reverse_sort2(l: list):
    ret = 0

    for i in range(len(l)):
        st = l[i]
        for t in range(i+1, len(l)):
            if st > l[t]:
                ret += 1

    return ret


l = [7, 5, 6, 4]
print(sum_reverse_sort(l))
print(sum_reverse_sort2(l))
