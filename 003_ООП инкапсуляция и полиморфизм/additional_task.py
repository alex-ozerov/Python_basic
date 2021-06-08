class Base():
    def method(self):
        print("Hello from Base")


class Child(Base):
    def method(self):
        print("Hello from Child")

def main():
    obj = Base()
    obj.method()
    obj = Child()
    obj.method()


if __name__ == "__main__":
    main()