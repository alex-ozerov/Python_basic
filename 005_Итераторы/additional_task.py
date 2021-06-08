class Myiter():
    def __init__(self, name):
        self.name = name

    def __iter__(self):
        self.i = -1
        return self

    def __next__(self):
        self.i += 1
        if self.i >= len(self.name):
            return
        return self.name[::-1][self.i]


list = Myiter([1, 2, 35, 46, 5])
list_iter = iter(list)
print(next(list))
print(next(list))
print(next(list))
print(next(list))
print(next(list))
print(next(list))