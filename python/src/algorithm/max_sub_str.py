def max_sub_str(s):
    start_index = 0
    max_length = 0
    temp_length = 0
    hashmap = {}

    for i in range(len(s)):
        st = s[i]
        if st not in hashmap or (st in hashmap and hashmap[st] < start_index):
            temp_length += 1
        else:
            start_index = i
            max_length = max_length if max_length > temp_length else temp_length
            temp_length = 1

        hashmap[st] = i

    return max_length if max_length > temp_length else temp_length


def max_sub_str2(s):
    def _fn(s, i):
        if i == 0:
            return (1, s[0])

        value = _fn(s, i - 1)
        if value[-1] == s[-1]:
            return len(value)

        return len(value) + 1

    return _fn(s, len(s) - 1)[0]


print(max_sub_str('arabcacfr'))
print(max_sub_str2('arabcacfr'))
