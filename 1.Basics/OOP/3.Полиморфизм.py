'''
Полиморфизм - это возможность использования одного и того же имени
операции или метода к объектам разных классов.
'''


# Родитеский класс
class A:
    def oper(self, x, y):
        return x + y


# Наследуем от класса "А"
class B(A):
    # Переопределяем метод oper из класса A
    def oper(self, x, y):
        return x / y


obj1 = A()
print(obj1.oper(2, 4))  # 6

obj2 = B()
print(obj2.oper(2, 4))  # 0.5
