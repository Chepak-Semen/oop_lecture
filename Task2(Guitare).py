"""Create two classes: Laptop, Guitare, one for composition, another one for aggregation."""


class Guitare:
    def __init__(self, strings):
        self.strings_count = strings


class String:
    def __init__(self, num, type_string):
        self.count_of_string = num
        self.type_of_string = type_string

    def talk(self):
        print(f"I`m guitar with {self.count_of_string.strings_count} strings and they are {self.type_of_string}")
