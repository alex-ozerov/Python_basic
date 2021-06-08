class Car():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def run(self):
        print(f"{self.name}: я могу ездить")

    def __repr__(self):
        return (f"name {self.name}, age {self.age}")

class Passenger_car(Car):
    def run(self):
        print(f"{self.name}: я могу ездить быстро")

class Cargo_car(Car):
    def carry_the_load(self):
        print(f"{self.name}: Я могу перевозить грузы")
toyota = Passenger_car("Toyota", "2018")
iveco = Cargo_car("Iveco", "2001")

print(toyota)
toyota.run()
print(iveco)
iveco.run()
iveco.carry_the_load()