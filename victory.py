# Задание
# Написать или улучшить программу Викторина из предыдущего дз
# (Для тренировки предлагаю не пользоваться никакими библиотеками кроме random)
# Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy')
# - предлагаю для тренировки пока использовать строку
# Программа выбирает из этих 10-и 5 случайных людей,
# это можно реализовать с помощью модуля random и функции sample
# Пример использования sample:
# import random
#
# numbers = [1, 2, 3, 4, 5]
#
# # 2 - количество случайных элементов
# result = random.sample(numbers, 2)
#
# print(result)
# [5, 1]
#
# После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
# пользователь вводит дату в формате 'dd.mm.yyyy'
#
# Например 03.01.2009, если пользователь ответил неверно,
# то выводим правильный ответ, но уже в следующем виде:
# третье января 2009 года, склонением можно пренебречь
#
# В конце считаем количество правильных
# и неправильных ответов и предлагаем начать снова

# Решение:
# Дано 10 композиторов
# Людовико Эйнауди 23 ноября 1955 (23.09.1955)
# Филип Гласс 31 января 1937 года (31.01.1937)
# Макс Рихтер 22 марта 1966 (22.03.1966)
# Джон Кейдж 5 сентября 1912 (05.09.1912)
# Игорь Стравинский 17 июня 1882 (12.06.1882)
# Тору Такэмицу 8 октября 1930 (08.10.1930)
# Георгий Свиридов 3 декабря 1915 (03.12.1915)
# Стивен Райх 3 октября 1936 (03.10.1936)
# Шнитке Альфред 24 ноября 1934 (24.11.1934)
# Ясуси Акутагава 12 июля 1925 (12.07.1925)

# импортируем рандом

import random

# допустим задан tuple из имен композиторов и дат
composers_tuple = ('Людовико Эйнауди', 'Филип Гласс', 'Макс Рихтер', 'Джон Кейдж',
                   'Игорь Стравинский', 'Тору Такэмицу', 'Георгий Свиридов', 'Стивен Райх',
                   'Альфред Шнитке', 'Ясуси Акутагава',)

date_tuple = ('23.09.1955', '31.01.1937', '22.03.1966', '05.09.1912', '12.06.1882', '08.10.1930',
              '03.12.1915', '03.10.1936', '24.11.1934', '12.07.1925')

text_year = ('23 ноября 1955', '31 января 1937 года', '22 марта 1966', '5 сентября 1912',
             '17 июня 1882', '8 октября 1930', '3 декабря 1915', '3 октября 1936',
             '24 ноября 1934', '12 июля 1925')

# формируем список
dict_all = zip(composers_tuple, date_tuple, text_year)
dict_all = list(dict_all)

# Число вопросов в викторине
number_of_composers = 5

print('Будет выбрано %s случайных композиторов для викторины:' % number_of_composers)
print('Угадайте дату рождения этих композиторов, вводите в формате dd.mm.yyyy(d- день, m - месяц, y - год)')

# Зацикливаем викторину
circle_victory = True

# Реализация программы
while circle_victory == True:
    # выводим 5-ть случайных композиторов
    shorten_random_composers = random.sample(dict_all, number_of_composers)

    # начальные значения счетчиков правильных и неправильных ответов
    bad_answers = 0
    good_answers = 0

    # это значение нужно для реализации того, чтобы программа спрашивала о продолжении
    circle_answers = True

    for composers in shorten_random_composers:
        user_input_date = str(input(f'Выбран {composers[0]} введите его год рождения : '))
        if user_input_date == composers[1]:
            print('Верно')
            good_answers += 1

        else:
            print('Не верно')
            print(f'Правильный ответ: {composers[2]}')
            bad_answers += 1

    proc_true = ((good_answers) * 100) / (number_of_composers)
    proc_false = ((bad_answers) * 100) / (number_of_composers)
    print('')
    print('Кол-во правильных ответов', good_answers)
    print('Кол-во неправильных ответов', bad_answers)
    print('Процент правильных ответов', proc_true)
    print('Процент неправильных ответов', proc_false)
    print('')
    while circle_answers == True:
        try:
            user_input_answer = str(input('Вы хотите попробовать снова? Введите да или нет: '))
            if user_input_answer == 'нет':
                print('выхожу...')
                circle_victory = False
                break
            elif user_input_answer == 'да':
                print('играем снова!')
                circle_answers = False
            else:
                raise ValueError
        except ValueError:
            print("Введите да или нет буквами")
