class Book:
    def __init__(self, name, author, age, fan):
        self.name = name
        self.author = author
        self.age = age
        self.fan = fan

    def __repr__(self):
        return f'Book {self.name}, author {self.author}, age {self.age}, fan {self.fan}'
    def __str__(self):
        return f'Book {self.name}, author {self.author}, age {self.age}, fan {self.fan}'

    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.name == other.name and
                    self.author == other.author and
                    self.age == other.age and
                    self.fan == other. fan)
        else:
            return NotImplemented


book1 = Book('Robinson Crusoe', 'Daniel Defo', '1719', 'adventure')
book2 = Book('Treasure island', 'Robert Louis Stevenson', '1883', 'adventure')
print(repr(book1))
print(repr(book2))
print(book1)
print(book2)
print(book1 == book2)
