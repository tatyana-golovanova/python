def gen(n):
    for i in range(n + 1):
        if i % 2 != 0:
            yield i


g = gen(7)
print(list(g))


def gen_2(n):
    return (i for i in range(n + 1) if i % 2 != 0)


g = gen_2(7)
print(list(g))
