# class is a template for an object

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 8)
# print(p.x)
# print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

peoples = ["Harry", "Ron", "Hermione", "Ginny"]
for person in peoples:
    if flight.add_passenger(person):
        print(f"{person} has been added to the flight.")
    else:
        print(f"{person} couldn't be added to the flight due to full capacity.")