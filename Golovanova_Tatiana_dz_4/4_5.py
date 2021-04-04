import sys

from utils import currency_rates


if __name__ == '__main__':
    _, *argv = sys.argv
    if len(argv) != 1:
        print("Код валюты введен неверно")
        sys.exit(1)
    result = currency_rates(argv[0])
    print(f"{result['quotation']}, {result['date']}")
