class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display_info(self):
        print(self.brand, self.speed)

class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

    def display_info(self):
        super().display_info()
        print("Doors:", self.doors)

class Motorcycle(Vehicle):
    def __init__(self, brand, speed, sidecar):
        super().__init__(brand, speed)
        self.sidecar = sidecar

    def display_info(self):
        super().display_info()
        print("Sidecar:", self.sidecar)

Car("Toyota", 180, 4).display_info()
print()
Motorcycle("Harley-Davidson", 140, True).display_info()