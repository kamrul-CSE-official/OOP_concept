class Car:
    name = ""
    color = ""

    def start():
        print("Starting the engine")

Car.name = "Axio"
Car.color = "Red"

print("Name of the Car: ", Car.name)
print("Color: ", Car.color)

Car.start()