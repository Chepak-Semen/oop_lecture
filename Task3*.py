"""Create metaclass with inheritance"""


class Meta(type):
    def __new__(mcs, name, bases, attrs):
        attrs[name] = bases
        return super().__new__(mcs, name, bases, attrs)


class U(metaclass=Meta):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    a = U()
    print(type(a))