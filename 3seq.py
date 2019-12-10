# Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
# Затем он вводит элементы 2-го списка
# Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
#
# Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
# Введите элементы 2-го списка: 2,5
# Результат: 1,3,4

# Создаем пустые списки
new_list_1 = []
new_list_2 = []
# Блок формирования списков new_list_1 и new_list_2
print('Вы хотите ввести элементы по очередно вручную или сразу готовой строкой? ')
input_type_check = input('Если поочередно введите: Да, а если в строку введите: Нет ')

if input_type_check == 'Да' or input_type_check == 'да':
    elements_amount_1 = int(input('Введите количество элементов первого списка '))
    for number in range(elements_amount_1):  # формирование new_list_1 поочередно
        number += 1  #
        element_input = input(('Введите № %s элемент ' % number))
        new_list_1.append(element_input)
    # print(new_list_1)
    elements_amount_2 = int(input('Введите количество элементов второго списка '))
    for number in range(elements_amount_2):  # формирование new_list_2 поочередно
        number += 1  #
        element_input = input(('Введите № %s элемент ' % number))
        new_list_2.append(element_input)
    # print(new_list_2)
elif input_type_check == 'Нет' or input_type_check == 'нет':
    new_list_1 = input('Введите цифровые элементы первого списка в строку через запятую: ')
    new_list_1 = new_list_1.split(',')  # формирование new_list_1 строкой
    print(new_list_1)
    new_list_2 = input('Введите цифровые элементы второго списка в строку через запятую: ')
    new_list_2 = new_list_2.split(',')  # формирование new_list_2 строкой
    # print(new_list_2)
# Удаление из списка new_list_1 элементы, которые есть в списке new_list_2
list_result = (sorted(set(new_list_1) - set(new_list_2)))
# str_result = list(list_result)
# print(str_result)
# print(*str_result, sep =', ')
print('Результат:', ','.join(list_result))  # делаем результат, как в примере
