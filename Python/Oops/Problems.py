class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
    
    def get_brand(self):
        return self.__brand
    def displayInfo(self):
        print(f"{self.get_brand()} and {self.model}")
    
    @property
    def model(self):
        return self.__model
    
class ElectricClass(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
        
# tesla = ElectricClass('tesla','s','100kwh')
# tesla.displayInfo()
# print(tesla.get_brand())
# print(f"{isinstance(tesla, ElectricClass)}")
# print(f"{isinstance(tesla, Car)}")
# my_car = Car(brand = "Swift", model = "2025")
# print(Car)
# my_car.displayInfo()

class Battery:
    def display_battery(self):
        print("Battery data")

class Engine:
    def display_engine(self):
        print("Engine data")
 
 
class HybridCar(Car,Engine,Battery):
    def __init__(self,brand,model,battery_size,engine_type):
        Car.__init__(self,brand,model)
        self.battery_size = battery_size
        self.engine_type = engine_type
    def displayInfo(self):
        print(f"{self.get_brand()} , {self.model} , {self.battery_size} , {self.engine_type}")
        
# my_hybrid
# my_hybrid
new_car    = HybridCar("Toyota","2024","50kwh","V6")

new_car.displayInfo()
new_car.display_battery()
new_car.display_engine()