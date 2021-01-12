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


class CanNotStealError(Exception):
    # custom error for Realtor
    pass


class NotEnoughMoney(Exception):
    # custom error
    pass


class Singleton(type):
    # create only one instance of class
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Home:
    """Home used in Realtor.
    It can be sold
    has price and discount"""

    def __init__(self):
        self.area = randint(25, 40)  # size of home
        self.cost = self.area * 600  # price of home

    def apply_discount(self, discount):
        """if realtor give discount
        this method will apply it
        and change self.cost"""
        self.cost -= self.cost * discount


class Human:
    """Human<-Person
    object Human work with Realtor """

    def __init__(self, name, age, money, have_home):
        self.name = name
        self.age = age
        self.money = money
        self.have_home = have_home  # availability of house in object human

    def __str__(self):
        # tell information about human
        return f'{20 * "_"}\n' \
               f'name : {self.name} \nage : {self.age} \nmoney : {self.money}$\nHave home : {self.is_home()}\n' \
               f'{20 * "_"}\n'

    def is_home(self):
        return 'I`ve Home' if self.have_home is True else 'I don`t have Home'

    def make_money(self):
        # if object human has not enough money he need make them,
        print(f'{self.name} make money')
        self.money += randint(1000, 5000)

    def can_buy(self, home: Home):
        if self.money >= home.cost:
            return True
        else:
            raise NotEnoughMoney

    def buy_house(self, home: Home):
        try:
            self.can_buy(home)
            print(f'{self.name} buy house {home} for {home.cost}$')
            self.money -= home.cost
            self.have_home = True
        except NotEnoughMoney:
            print(f'{self.name} can`t buy a house {home} because he need {home.cost - self.money}$ more')


class Person(Human):
    """Human<-Person"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.money = randint(10000, 20000)
        self.have_home = False
        super(Person, self).__init__(self.name, self.age, self.money, self.have_home)  # transfer data to Human __init__


class Realtor(metaclass=Singleton):
    """Realtor has only one instance
    He can sell house to Human"""

    def __init__(self, name, client: Person):
        self.name = name
        self.houses = [Home() for _ in range(randint(1, 10))]  # list of Home
        self.discount = randint(1, 20)
        self.client = client

    def houses_info(self):
        print(f'{20 * "_"}\nRealtor has a houses:')
        for i in self.houses:
            print(f'House{self.houses.index(i) + 1} {i.area}m^2 and it cost {i.cost}$')
        print(f'{20 * "_"}')

    def give_discount(self):
        print(f'Realtor: I give you a {self.discount}% discount for house you want')
        return self.discount / 100

    @staticmethod
    def chance():
        if randint(1, 10) == 1:  # 10% chance
            return True
        else:
            raise CanNotStealError

    def steal(self):
        try:
            self.chance()
            self.client.money = 0
            print(
                f'Realtor {self.name} steal the money in {self.client.name},'
                f' and {self.client.name} has left {self.client.money}$')
        except CanNotStealError:
            print(f'Realtor {self.name} could not steal money in {self.client.name}')


if __name__ == '__main__':
    person_Tom = Person(name='Tom', age=34)
    realtor_Sasha = Realtor(name='Sasha', client=person_Tom)
    print(person_Tom)
    person_Tom.make_money()
    print(person_Tom)
    realtor_Sasha.houses_info()
    realtor_Sasha.steal()
    house = choice(realtor_Sasha.houses)
    house.apply_discount(realtor_Sasha.give_discount())
    realtor_Sasha.houses_info()
    person_Tom.buy_house(house)
    realtor_Sasha.houses.remove(house)
    print(person_Tom)
