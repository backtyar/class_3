# Создайте симулятор магазина, включая классы Product, Customer, Cart и Store.
# Класс Product должен иметь атрибуты, такие как название, цена и количество на
# складе. Класс Customer представляет клиента и имеет атрибут cart для добавления
# товаров. Класс Store управляет инвентарем и покупками. Реализуйте функциональность
# добавления товаров в корзину, расчет общей суммы и обновление инвентаря.

class Product:

    def __init__(self, name, price, quantity_stock):
        self.name = name
        self.price = price
        self.quantity_stock = quantity_stock

    def __repr__(self):
        return f'{self.name}, {self.price}, {self.quantity_stock}'

banana = Product('banana', 150, 5)
orange = Product('orange', 200, 10)
onion = Product('onion', 200, 15)


class Customer:
    def __init__(self, client_name):
        self.client_name = client_name
        self.cart = []

    def add_cart(self, product):
        self.cart.append(product)

anna = Customer('Anna')
anna.add_cart(banana)
anna.add_cart(onion)
anna.add_cart(orange)

class Cart:
    pass

class Story:
    pass





# Создайте приложение для управления задачами. Реализуйте классы Task, TaskList,
# и User. Task должен иметь атрибуты, такие как название, описание и статус
# (выполнено/не выполнено). TaskList содержит список задач, и методы для
# добавления, удаления и фильтрации задач. Класс User хранит информацию о
# пользователях и их списки задач. Реализуйте возможность регистрации и
# авторизации пользователей.

# class Task:
#
#     def __init__(self, name, ops, status, level):
#         self.name = name
#         self.ops = ops
#         self.status = status
#         self.level = level
#
# class TaskList:
#
#     def __init__(self):
#         self.task_list = []
#
#     def add_task(self, task):
#         self.task_list.append(task)
#
#     def del_task(self, task):
#         self.task_list.remove(task)
#
#     def filter_task(self):
#         res = sorted(self.task_list)
#         for i in res:
#             print(i)
#


#
# class User:
#     __password = {}
#     def __init__(self, task_list):
#         self.user = ''
#         self.task_list = task_list
#
#     def __registration(self):
#         self.user = input('Name: ').strip()
#         password = input('password: ').strip()
#         User.__password[self.user] = password
#         self.access_task()
#
#
#
#     def __authorization(self):
#         password = input('Введите пороль: ').strip()
#         if User.__password[self.user] == password:
#             self.__decide_task()
#
#
#     def __decide_task(self):
#         print('00000000')
#         return '0000000000000'
#
#
#     def access_task(self):
#         if self.user == '':
#             self.__registration()
#         else:
#             self.__authorization()
#
# u = User([])
# u.access_task()
