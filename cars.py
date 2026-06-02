class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"(Car: {self.brand} {self.model}"

car = Car("BMW", "M4")
print(car)