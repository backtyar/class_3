# Создайте симулятор магазина, включая классы Product, Customer, Cart и Store.
# Класс Product должен иметь атрибуты, такие как название, цена и количество на
# складе. Класс Customer представляет клиента и имеет атрибут cart для добавления
# товаров. Класс Store управляет инвентарем и покупками. Реализуйте функциональность
# добавления товаров в корзину, расчет общей суммы и обновление инвентаря.
#
class Product:

    def __init__(self, name, price, quantity_stock):
        self.name = name
        self.price = price
        self.quantity_stock = quantity_stock

    def __repr__(self):
        return f'{self.name}, {self.price}, {self.quantity_stock}'




class Customer:
    def __init__(self, client_name, quantity):
        self.__client_name = client_name
        self.__cart = []
        self.quantity = quantity
        self.total = []

    def add_cart(self, product):
        self.__cart.append(product)


    def __str__(self):
        for i in self.__cart:
            self.total.append(i.price * self.quantity)
        return f'{self.total}'




class Store:
    __product_story = {}

    def __init__(self, client):
        self.client = client
        self.product_class = Product
        self.client_customer = []


    def add_cart_customer(self, name, quantity):
        if name in Store.__product_story:
            customer = Customer(self.client, quantity)
            customer.add_cart(Store.__product_story[name])
            self.client_customer.append(customer)
            print(customer)
        else:
            return 'Not product'

    @classmethod
    def add_product_story(cls, name, price, quantity):
        product = Product(name, price, quantity)
        Store.__product_story[product.name] = product



s = Store('Anna')
Store.add_product_story('banana', 150, 100)
Store.add_product_story('orange',  100, 100)
Store.add_product_story('onion', 150, 100)
s.add_cart_customer('onion',5)
s.add_cart_customer('banana',10)






# Создайте приложение для управления задачами. Реализуйте классы Task, TaskList,
# и User. Task должен иметь атрибуты, такие как название, описание и статус
# (выполнено/не выполнено). TaskList содержит список задач, и методы для
# добавления, удаления и фильтрации задач. Класс User хранит информацию о
# пользователях и их списки задач. Реализуйте возможность регистрации и
# авторизации пользователей.

class Task:
    def __init__(self, name, ops, status, level=1):
        self.name = name
        self.ops = ops
        self.level = level
        if status == True:
            self.status = '✅'
        else:
            self.status = '-'

task_1 = Task('Сумма','Целочисленная арифметика',False,5)
task_2 = Task('Пятью пять - двадцать пять!','Целочисленная арифметика',True,2)
task_3 = Task('Статистика','Сортировка и последовательности',True,3)
task_4 = Task('Золото племени АББА','Длинная арифметика',False,8)
task_5 = Task('Лесенка','Рекурсия, перебор',True,5)

class TaskList:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def del_task(self, task):
        self.task_list.remove(task)

    def filter_task(self):
        return sorted(self.task_list, key=lambda x: x.level)

ts_1 = TaskList()
ts_1.add_task(task_1)
ts_1.add_task(task_2)
ts_1.add_task(task_3)
ts_1.add_task(task_4)
ts_1.add_task(task_5)


class User:
    __password = {}
    def __init__(self, task_list):
        self.user = ''
        self.task_list = task_list

    def __registration(self):
        print('зополните поля для регистрации')
        self.user = input('Name: ').strip()
        password = input('password: ').strip()
        User.__password[self.user] = password
        self.access_task()

    def __authorization(self):
        print(f'Пользователь {self.user}')
        password = input('Введите пороль: ').strip()
        if User.__password[self.user] == password:
            self.__decide_task()


    def __decide_task(self):
        print('Можете приступить к решению задач')



    def access_task(self):          # пользователь получает доступ к задачам  через функцию access_task
        if self.user == '':         #
            self.__registration()   # перенопровляеть __registration
        else:
            self.__authorization()  # перенопровляеть __authorization

    def info_users(self):
        if self.user != '':
            print(f'Пользователь: {self.user}')
            for tusk in self.task_list:
                print(f'Называние:{{{tusk.name}}}, описание: {{{tusk.ops}}},'
                      f'статус: {{{tusk.status}}}, уровень: {{{tusk.level}}}')
            else:
                return ''






anna = User(ts_1.filter_task())     # добавляем список задач к классу User с помощью ts_1.filter_task() - эгземпляр класса TaskList
anna.access_task()
print('*' * 50)
anna.info_users()



