'''
Список (list) в Python - это коллекция, в которой хранится набор элементов.
Он определяется в квадратных скобках [], где через запятую перечисляются его элементы.
Списки Python похожи на массивы в других языках (С++, Java).
'''

# Создадим список с произвольными значениями.
mylist = [1, "два", 3.1]

# Получение элемента списка по индексу mylist[0]
# где 0 порядковый номер элемента (нумерация начинается с 0)
print("first: ", mylist[0])

# len() - возвращает число элементов в списке (длину списка)
print("Число элементов в списке = ", len(mylist))

# append() - добавляет элемент в конец списка
mylist.append("new")  # Добавляем новый элемент в конец списка
mylist += ["new2"]  # Альтернативный вариант
print("Add: ", mylist)

# pop() - удаление элемента в списке по индексу
mylist.pop(0)  # Удаляем первый элемент
print("Del: ", mylist)

# remove() - удаление элемента по значению
mylist.remove("new")
print("Del: ", mylist)
'''
Вырезание a[первый индекс: предпоследний индекс]
если индексы не прописывать, а оставить просто a[:],
первоначальный индекс автоматически станет  равен 0,
последний - количество элементов)
'''
a = a = [1, 1, 2, 3, 2, 4]
c = a[1:3]  # c=  [1, 2]
print("c =", c)

# Удаление повторений
a = [1, 2, 3, 2, 4, 4]
c = set(a)
print("set() =", c)

# Сортировка
a = [9, 1, 2, 3, 3, 2, 1, 10]
# Sorted - Создается новый упорядоченный массив
c = sorted(a)
print("sorted =", c)

# Sort упорядочивает элементы текущего массива
a.sort()
print("sort =", a)

# Преобразует все элементы массива（mapping）
# используем лямбда-выражение увеличивающее значение на 1.
# list преобразует вывод функции map в список
c = list(map(lambda x: x + 1, a))
print("+1 =", c)

# Фильтр
# Ищется элементы、которые делится на два без остатка.
# Подходящие элементы образуют новый массив.
a = a = [1, 2, 3, 2, 4, 4]
c = list(filter(lambda x: x % 2 == 0, a))
print("%2 =", c)
# -----------------------------------------------

# Вложенные списки
# Список также может в качестве элемента включать в себя другой список
superlist = [[1, 2, 3], [4, 5, 6]]
print(superlist)

# Для получения элементов вложенных списков используем двойной индекс.
# Получаем второй элемент второго списка.
print(superlist[1][1])

# insert(index, item) - добавляет элемент item в список по индексу index,
# clear() - удаление всех элементов из списка,
# index(item) - возвращает индекс элемента item,
# count(item) - количество элементов item в списке,
# sort([key]) - сортирует элементы (с помощью параметра key мы можем передать функцию сортировки),
# reverse() - элементы в списке в обратном порядке,
# min(list) - наименьший элемент списка,
# max(list) - наибольший элемент списка.
