# Комментарии пишутся после символа '#'.
'''
или в блоке ограниченом тремя апострофами 

'''

# Переменная задается выражением имя = значение
i = 10
txt = "Привет мир!"
# При назначении переменная имеет тип советующий значению. Так i является числом (int), а txt строкой (str).

# Когда хотим определить тип, используем type
print(type(i))  # <class 'int'>
print(type(txt))  # <class 'str'>

# Переменная не сохраняет, а ссылается на значение
# Это, своего рода, переменная-ссылка, указывающая на местоположение значения
# Можно получить идентификатор актуального значения через id
print(id(i))
i2 = i
print(id(i2))  # то же значение, что у вышеуказанного id(l))
# Поскольку существует только одно значение, на которое ссылаются переменные i и i2.

# Типы данных python:
# int - представляет целое число 1, 2, 100 и тд.
i = 10

# str - строки представляют набор символов в кодировке Unicode
s = "Привет мир!"

# bool - логический тип (boolean), может быть True(Истина) или False(Лож)
b = True  # логический тип (boolean)

# list - список
l = [1, 'два', 3.1]

# tuple - кортеж
t = ('Первый', 'Второй', 'Третий')

# dict - словарь, каждый элемент имеет пару ключ и значение
d = {1: 'Первый', 2: 'Второй'}

# float - представляет число с плавающей точкой
f = 3.14

# complex - комплексные числа
# bytes - последовательность чисел в диапазоне 0-255
# bytearray - массив байтов, аналогичен bytes с тем отличием, что может изменяться
# set - неупорядоченная коллекция уникальных объектов
# frozen set - то же самое, что и set, только не может изменяться (immutable)

# Арифметические операции
a = a + b  # Сложение. Складывает а и b и присваивает значение переменной a
a = a - b  # Вычитание
a = a * b  # Умножение
a = a / b  # Деление
# Иногда бывает полезна краткая запись
a += 1  # значение увеличивается на 1 (a = a + 1)
a -= 1  # значение уменьшается на 1 (a = a - 1)
a *= 2  # значение увеличивается в два раза (a = a * 2)
a /= 3  # значение составляет ⅓ предыдущего значения (a = a / 3)

# Логические выражения возвращают значения True или False

# == - Сравнение. Вернет True если равно
print("1 == 1 - ", 1 == 1)

# != - НЕ равно. Вернет True  НЕ если равно
print("1 != 2 - ", 1 != 2)

# < - Меньше
print("1 < 2 - ", 1 < 2)  # True

# > - Больше
print("1 > 2 - ", 1 > 2)  # False

# <= - Меньше либо равно
print("1 <= 1 - ", 1 <= 1)  # True

# >= - Больше либо равно
print("1 >= 2 - ", 1 >= 2)  # False

# Отступы
'''
Большинство языков программирования, таких как C, C++, Java, используют фигурные скобки {} для определения блока кода. В отличии от них, Python использует отступы. В Python, как правило, используются четыре пробела для выделения блока кода
'''
if True:
    s = 'World'
    print('Hello', s)

# Отступы можно игнорировать если разделять строки кода точкой с запятой.
if True:
    s = 'World'
    print('Hello', s)
# Это не вызовет ошибок однако это является плохой практикой потому что снижает читабельность вашего кода.
