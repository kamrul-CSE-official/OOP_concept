class Car: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start(self):
        print("Name: ",self.name)
        print("Color: ",self.color)
        print("Starting the engine")

my_car = Car("Corolla", "Black")
my_car.start()