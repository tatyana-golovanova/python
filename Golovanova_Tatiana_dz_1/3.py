percent = "процент"
number = 1
if number == 1:
    ending = ""
elif number in [2, 3, 4]:
    ending = "а"
else:
    ending = "ов"

print(str(number) + " " + percent + ending)
