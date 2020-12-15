class Vehicle:
     def __init__(self, make, model, year):
          self.make = make
          self.model = model
          self.year = year
     def vehicle_info(self):
          print(self.make, self.model, self.year)

car1 = Vehicle("Nissan", "GTR", "1990")
car2 = Vehicle("BMW", "M4", "2020")

car1.vehicle_info()
car2.vehicle_info()