class User:
    def __init__(self, salary, work_hours):
        self.salary = salary
        self.work_hours = work_hours

    def hour_price(self):
        return self.salary / self.work_hours

    def minute_price(self):
        return self.hour_price() / 60


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def work_time(self, user):
        hours = self.price / user.hour_price()
        minutes = self.price / user.minute_price()

        print('Вам нужно работать', round(hours, 1), 'часов')
        print('или', round(minutes), 'минут')


salary = int(input('Введите вашу зарплату: '))
work_hours = int(input('Введите количество рабочих часов в месяц: '))

user = User(salary, work_hours)


coffee = Product('Кофе', 300)
burger = Product('Бургер', 350)
cinema = Product('Кино', 500)
sneakers = Product('Кроссовки', 10000)
airpods = Product('AirPods', 15000)
iphone = Product('iPhone', 100000)
macbook = Product('MacBook', 200000)
car = Product('Машина', 1500000)
apartment = Product('Квартира', 15000000)


print('Выберите товар:')

print('1. Кофе')
print('2. Бургер')
print('3. Кино')
print('4. Кроссовки')
print('5. AirPods')
print('6. iPhone')
print('7. MacBook')
print('8. Машина')
print('9. Квартира')


while True:

    choice = (input('Введите номер товара: '))

    if choice == '1':
        coffee.work_time(user)

    elif choice == '2':
        burger.work_time(user)

    elif choice == '3':
        cinema.work_time(user)

    elif choice == '4':
        sneakers.work_time(user)

    elif choice == '5':
        airpods.work_time(user)

    elif choice == '6':
        iphone.work_time(user)

    elif choice == '7':
        macbook.work_time(user)

    elif choice == '8':
        car.work_time(user)

    elif choice == '9':
        apartment.work_time(user)

    else:
        print('Неверный выбор')
