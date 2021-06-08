class Car():
    def __init__(self, name, age, mileage):
        self.name = name
        self.age = age
        self._mileage = mileage

    def run(self):
        print(f"{self.name}: я могу ездить")

    def get_mileage(self):
        print(f"new mileage:{self._mileage}")

    def set_mileage(self, mileage):
        self._mileage = mileage

    def __repr__(self):
        return (f"name: {self.name}, age: {self.age}, odometer: {self._mileage}")


toyota = Car("Toyota", "2018", "100")

print(toyota)
toyota.run()
toyota.set_mileage(2000)
toyota.get_mileage()
