class Car: 
    def __init__(self, name, colore) :
        self.name = name
        self.colore = colore

    def start(self):
        print("Name: ", self.name)
        print("Colore: ", self.colore)
        print("Starting the engine")

my_car1 = Car("Corolla", "White")
my_car1.start()

my_car2 = Car("Corolla", "Black")
my_car2.start()

my_car3 = Car("Corolla", "Blue")
my_car3.start()