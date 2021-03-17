duration = 400153
result = ""

seconds = duration % 60
result += str(seconds) + " сек"

minutes = duration // 60
if minutes > 0:
    result = str(minutes % 60) + " мин " + result

    hours = minutes // 60
    if hours > 0:
        result = str(hours % 24) + " час " + result

        days = hours // 24
        if days > 0:
            result = str(days) + " дн " + result

print(result)
