def nums_of_one(n):
    ret = 0

    def get_one_sum(i):
        num = 0

        while i:
            value = i % 10
            if value == 1:
                num += 1
            i = (i - value) / 10

        return num

    for i in range(1, n + 1):
        ret += get_one_sum(i)

    return ret


print(nums_of_one(15))



