TRANSLATES = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}


def num_translate(word):
    return TRANSLATES.get(word)


print(num_translate('two'))
print(num_translate('twenty'))


def num_translate_adv(word):
    islower = word.islower()
    result = num_translate(word.lower())

    if result is not None and not islower:
        result = result.capitalize()
    return result


print(num_translate_adv('Two'))
print(num_translate_adv('One'))
print(num_translate_adv('four'))
