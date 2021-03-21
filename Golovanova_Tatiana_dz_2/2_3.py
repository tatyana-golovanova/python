my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
signs = ('+', '-')

for i, item in enumerate(my_list):
    sign = ''
    for s in signs:
        if item.startswith(s):
            sign = s
            item = item[1:]

    if item.isdigit():
        # Обособила кавычками сразу в шаблоне, т.к. добавление кавычек как элементов массива
        # приводит к более сложному решению (с тем же результатом).
        my_list[i] = f'"{sign}{int(item):02}"'

print(' '.join(my_list))
