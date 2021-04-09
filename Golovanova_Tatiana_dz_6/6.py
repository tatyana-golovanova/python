import sys


if __name__ == '__main__':
    _, *args = sys.argv
    args_len = len(args)

    if args_len == 0:
        with open('sales.txt', 'r') as sales:
            for sale in sales.readlines():
                print(sale.strip())

    elif args_len <= 2:
        start_sale = args[0]
        end_sale = None
        if args_len == 2:
            end_sale = args[1]

        with open('sales.txt', 'r') as sales:
            print_f = False
            for sale in sales.readlines():
                sale = sale.strip()
                if sale == start_sale:
                    print_f = True
                if print_f:
                    print(sale)
                if sale == end_sale:
                    print_f = False

    else:
        print('Слишком много аргументов.')
        sys.exit(1)
