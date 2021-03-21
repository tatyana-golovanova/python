prices = [57.8, 46.51, 97, 1500, 105.80, 100, 58.90, 8, 300, 10]

# Часть А
prices_str = []
for item in prices:
    prices_in_kop = int(item * 100)
    rubles, kopeks = divmod(prices_in_kop, 100)
    prices_str.append(f'{rubles} руб {kopeks:02} коп')
print(', '.join(prices_str))

# Часть В
print(id(prices))
prices.sort()
print(prices)
print(id(prices))

# Часть C
prices_revers = sorted(prices, reverse=True)
print(prices_revers)

# Часть D
print(prices_revers[:5][::-1])
