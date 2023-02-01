list_data = input().split()
int_lst = []
for element in list_data:
    if element.isdigit():
        int_lst.append(int(element))
    else:
        print(f'{element} - не является числом! ')
        print('Ошибка формирования списка чисел!')
        exit()
print(f'Ваш список чисел:', int_lst)