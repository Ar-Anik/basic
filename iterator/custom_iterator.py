class CustomIterator:
    def __init__(self, data):
        if isinstance(data, dict):
            self.items = list(data.keys())
        elif isinstance(data, (set, list, tuple, str)):
            self.items = list(data)
        else:
            raise TypeError("Unsupported type for Custom Iterator")

        self.index = 0

    def __iter__(self):
        print("--- return object ---")
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        value = self.items[self.index]
        print("Index Value : ", self.index)
        self.index += 1
        return value

lst_1 = CustomIterator([10, 20, 30])

print(lst_1.__next__())
print(lst_1.__next__())
print(lst_1.__next__())
# print(lst_1.__next__())

lst_2 = CustomIterator([100, 200, 300])
for x in lst_2:
    print(x)


dct_1 = CustomIterator({'a': 99, 'b': 97, 'c': 95})
print(dct_1.__next__())
print(dct_1.__next__())
print(dct_1.__next__())
# print(dct_1.__next__())

dct_2 = CustomIterator({'a': 11, 'b': 13, 'c': 17})
for x in dct_2:
    print(x)
