class MainClass:
    _instances = {}

    def __new__(cls, value):
        if value in cls._instances:
            return cls._instances[value]
        else:
            instance = super().__new__(cls)
            cls._instances[value] = instance
            return instance

    def __init__(self, value):
        self.value = value

a = MainClass(20)
b = MainClass(50)
c = MainClass(20)

print(id(a))
print(id(b))
print(id(c))

print(a is c)
