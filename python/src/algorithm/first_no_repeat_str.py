def first_no_repeat_str(s: str):
    ret = None
    has_repeat = False
    filter_list = []

    for i in range(len(s)):
        ret = s[i]
        for j in range(i+1, len(s)):
            if s[j] == ret:
                has_repeat = True
                filter_list.append(ret)
                ret = ''
                break

        if has_repeat:
            filter_list.append(s[i])
            has_repeat = False
            continue
        elif ret not in filter_list:
            return ret


def first_no_repeat_str2(s: str):
    hashmap = {}

    for i in range(len(s)):
        st = s[i]

        if st in hashmap:
            hashmap[st] += 1
        else:
            hashmap[st] = 1

    for st in s:
        if st in hashmap and hashmap[st] == 1:
            return st

    return None


print(first_no_repeat_str('abaccdeffb'))
print(first_no_repeat_str2('abaccdeffb'))
