cubes = []

# Создала список кубов нечетных чисел.
for number in range(1, 1001):
    if number % 2 != 0:
        cubes.append(number ** 3)

# Разделила каждое число на разряды и проверила, делится ли полученная сумма на 7 нацело.
sum_ = 0
for cube in cubes:
    ranks = []
    tmp = cube
    while tmp:
        ranks.insert(0, tmp % 10)
        tmp //= 10

    if sum(ranks) % 7 == 0:
        sum_ += cube

print(sum_)

# Предыдущий блок кода только без создания нового списка.
for idx, cube in enumerate(cubes):
    cubes[idx] = cube + 17

sum_2 = 0
for cube in cubes:
    ranks = []
    tmp = cube
    while tmp:
        ranks.insert(0, tmp % 10)
        tmp //= 10

    if sum(ranks) % 7 == 0:
        sum_2 += cube

print(sum_2)
