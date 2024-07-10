class Car:
    def __init__(self, color, speed, max_passengers, current_passengers):
        self.color = color
        self.speed = speed
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def get_color(self):
        return self.color
    
    def get_distance_traveled(self, time):
        return self.speed*time
    
    def add_passenger(self):
        if self.current_passengers<self.max_passengers:
            self.current_passengers += 1
        else:
            print("Maximum capacity of passengers.")
            return False
        return True

    def remove_passenger(self):
        if self.current_passengers>0:
            self.current_passengers -= 1
        else:
            print("There are already 0 passengers.")
            return False
        return True

car1 = Car("Red", 60, 1, 0)
print(car1.get_color()=="Red")
print(car1.remove_passenger()==False)
print(car1.get_distance_traveled(3)==180)
print(car1.add_passenger()==True)
print(car1.add_passenger()==False)