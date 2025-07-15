# custom iterable
class CustomList:
    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError("Custom List Expects a list")
        self.data = data

    def __iter__(self):
        print("--Create Iterator--")
        return CustomIterator(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)


# custom iterator
class CustomIterator:
    def __init__(self, data):
        if isinstance(data, dict):
            self.items = list(data.keys())
        elif isinstance(data, (set, list, tuple, str)):
            self.items = list(data)
        else:
            raise TypeError("Unsupported Type for Custom Iterator")

        self.index = 0

    def __iter__(self):
        print("---return object---")
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        value = self.items[self.index]
        print("Index Value : ", self.index)
        self.index += 1
        return value


obj = CustomList([10, 20, 30, 40])
for item in obj:
    print(item)

lst = CustomList([3, 5, 7, 11])
itr = iter(lst)

while True:
    try:
        item = next(itr)
        print(item)
    except StopIteration:
        break
