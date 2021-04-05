src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def pairs(iterable):
    idx = 0
    iterable_len = len(iterable) - 1
    while idx < iterable_len:
        yield iterable[idx:idx+2]
        idx += 1


def more(iterable):
    result = []
    for f, s in pairs(iterable):
        if s > f:
            result.append(s)
    return result


print(more(src))
