"""Create a class hierarchy of animals with at least 5 animals that have additional methods each."""


class Animal:
    @staticmethod
    def grow():
        print("I am growing up")

    @staticmethod
    def eat():
        print("I am eating")

    @staticmethod
    def move():
        print("I am moving on the ground")

    @staticmethod
    def can_breath():
        print('I am breathing')


class Fish(Animal):

    @staticmethod
    def move():
        print("I am swimming, I can`t move on the ground")

    @staticmethod
    def can_breath():
        print('I can`t breathe oxygen')


class Bird(Animal):

    @staticmethod
    def can_fly():
        print('I am flying')


class Shark(Fish):
    @staticmethod
    def eat():
        print("I hunt to eat")

    @staticmethod
    def is_predator():
        print("Yes, I`m a predator")


class Marlin(Fish):
    @staticmethod
    def was_in_book():
        print("Yes, i was a 'main' hero in 'Old and sea'")


class Eagle(Bird):
    @staticmethod
    def is_predator():
        print("Yes, I`m a predator, i like eat rabbits")


class Falcon(Bird):
    @staticmethod
    def is_predator():
        print("Yes, I`m a predator, i like eat rats")


class Parrot(Bird):
    @staticmethod
    def can_sing():
        print("Yes, I`m singing")
