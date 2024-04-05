class Car: 
    def __init__(self, name, colore):
        self.name = name
        self.colore = colore

    def start(self):
        print("Starting the engine")

car = Car("Corolla", "White")
print(car.name, car.colore)

car.year = 2024
print(car.year, car.name, car.colore)