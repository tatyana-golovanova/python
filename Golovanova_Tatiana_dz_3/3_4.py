from pprint import pprint


def thesaurus(*args):
    result = {}
    for name in args:
        result.setdefault(name[0], []).append(name)

    return result


pprint(thesaurus("Иван", "Мария", "Петр", "Илья"))


# задание 4*
def thesaurus_adv(*args):
    result = {}
    for item in args:
        name, surname = item.split()
        result.setdefault(surname[0], {}).setdefault(name[0], []).append(item)

    return result


pprint(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
