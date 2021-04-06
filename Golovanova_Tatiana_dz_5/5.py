scr = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

scr_1 = set(scr)
#print(scr_1)
result = []

for i in scr:
    if i in scr_1 and i in result:
        result.remove(i)
    else:
        result.append(i)

print(result)
