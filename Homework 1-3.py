# 1. Из всех методов списка (list) выбрать 5 тех, которые по вашему мнению используются чаще всего
# 2. Написать их через запятую с параметрами
# 3. Повторить процедуру для словарей (dict), множеств (set), строк (str)

# Решение

# 1. Списки (list)

# Выбрали возможные 5 наиболее встречающихся
# list.append(x) Добавляет элемент в конец списка
# list.extend(L) Расширяет список list, добавляя в конец все элементы списка L
# list.count(x) Возвращает количество элементов со значением x
# list.insert(y, 'x') Добавление в список 'x' на y место
# list.remove('x') Удаление 'x'

# 2. Перечислили их через запятую методы для списков (list)
list.append(x), list.extend(L), list.count(x), list.insert(y, 'x'), list.remove('x')

# 3.
# 3.1 Cловари (dict)
# Выбрали возможные 5 наиболее встречающихся
# dict.items() - возвращает пары (ключ, значение).
# dict.keys() - возвращает ключи в словаре.
# dict.values() - возвращает значения в словаре.
# dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются.
# dict.copy() - возвращает копию словаря.

# Перечислили их через запятую методы для словарей (dict)
dict.items(), dict.keys(), dict.values(), dict.update([other]), dict.copy()

# 3.2 Множества (set)
# set.isdisjoint(other) - истина, если set и other не имеют общих элементов.
# set.union(other, ...) или set | other | ... - объединение нескольких множеств.
# set.intersection(other, ...) или set & other & ... - пересечение.
# set.difference(other, ...) или set - other - ... - множество из всех элементов set, не принадлежащие ни одному из other.
# set.add(elem) - добавляет элемент в множество.

# Перечислили их через запятую методы для множеств (set)
set.isdisjoint(other), set.union(other, one), set.intersection(other, one), set.difference(other, one), set.add(elem)

# 3.3 Строки (str)
# S.split(символ) Разбиение строки по разделителю
# S.isdigit()	Состоит ли строка из цифр
# S.replace(шаблон, замена) Замена шаблона
# S.isalnum()	Состоит ли строка из цифр или букв
# S.join(список)	Сборка строки из списка с разделителем S///

# Перечислили их через запятую методы для строк (str)
S.split(символ), S.isdigit(), S.replace(шаблон, замена), S.isalnum(), S.join(список)