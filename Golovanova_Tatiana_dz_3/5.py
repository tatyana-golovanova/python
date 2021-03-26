import random


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    """
    Функция возвращающая n случайных шуток.

    :param n: Количество шуток для генерации.
    :return: Список шуток.
    """

    jokes = []
    for i in range(n):
        words = map(random.choice, (nouns, adverbs, adjectives))
        joke = ' '.join(words)
        jokes.append(joke)
    return jokes


print(get_jokes(6))
