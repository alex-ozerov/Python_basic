class English():
    def _greeting(self):
        print("hello friend")


class Spanish():
    def _greeting(self):
        print("Hola amigo")


obj1 = English()
obj2 = Spanish()


def hello_friend():
    obj1._greeting()
    obj2._greeting()

hello_friend()