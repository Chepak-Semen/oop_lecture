"""
There is a Person whose characteristics are:
1. Name
2. Age
3. Availability of money
4. Having your own home

Human can:
1. Provide information about yourself
2. Make money
3. Buy a house

There is also a House, the properties of which include:
1. Area
2. Cost

For Home you can:
1. Apply a purchase discount

e.g.: There is also a Small Typical House with a required area of 40m2.

*Realtor:
1. Name
2. Houses
3. Discount that he/she can give you.

*There is only one realtor who handles small houses you wanna buy. (Singleton)
Realtor is only one in your city and can:
1. Provide information about all the Houses
2. Give a discount
3. Steal your money with 10% chance
"""
from random import randint, choice


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Home:
    def __init__(self):
        self.area = randint(25, 40)
        self.cost = self.area * 600

    def apply_discount(self, discount):
        self.cost -= self.cost * discount


class Human:

    def __init__(self, name, age, money, have_home):
        self.name = name
        self.age = age
        self.money = money
        self.have_home = have_home

    def is_home(self):
        return 'I`ve Home' if self.have_home is True else 'I don`t have Home'

    def get_info(self):
        print(
            f'-My name is {self.name}, I`m {self.age} years old. I have {self.money}$, {self.is_home()}')

    def make_money(self):
        print(f'{self.name} make money')
        self.money += randint(1000, 5000)

    def buy_house(self, home: Home):
        if self.money > home.cost:
            print(f'{self.name} buy house {house} for {house.cost}$')
            self.money -= house.cost
            self.have_home = True
        else:
            print(f'{self.name} can`t buy a house {house} because he need {house.cost - self.money}$ more')


class Person(Human):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.money = randint(20000, 20000)
        self.have_home = False
        super(Person, self).__init__(self.name, self.age, self.money, self.have_home)


class Realtor(metaclass=Singleton):
    def __init__(self, name, client: Person):
        self.name = name
        self.houses = [Home() for _ in range(randint(1, 10))]
        self.discount = randint(1, 20)
        self.client = client

    def houses_info(self):
        print(f'Realtor has a houses:')
        for i in self.houses:
            print(f'House{self.houses.index(i) + 1} {i.area}m^2 and it cost {i.cost}$')

    def give_discount(self):
        print(f'Realtor: I give you a {self.discount}% discount for house you want')
        return self.discount / 100

    def steal(self):
        if randint(1, 10) == 1:
            self.client.money = 0
            print(
                f'Realtor {self.name} steal the money in {self.client.name},'
                f' and {self.client.name} has left {self.client.money}$')
        else:
            print(f'Realtor {self.name} could not steal money in {self.client.name}')


if __name__ == '__main__':
    person_Tom = Person(name='Tom', age=34)
    realtor_Sasha = Realtor(name='Sasha', client=person_Tom)
    person_Tom.get_info()
    person_Tom.make_money()
    person_Tom.get_info()
    realtor_Sasha.houses_info()
    realtor_Sasha.give_discount()
    realtor_Sasha.steal()
    house = choice(realtor_Sasha.houses)
    house.apply_discount(realtor_Sasha.give_discount())
    realtor_Sasha.houses_info()
    person_Tom.buy_house(house)
    realtor_Sasha.houses.remove(house)
    person_Tom.get_info()
