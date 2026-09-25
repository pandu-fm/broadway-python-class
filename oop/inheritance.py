"""
To inherit the property and methods from parent class.
"""

class School:

    def __init__(self, holiday_timing):
        self.exam_fee = 2000
        self.holiday_timing = holiday_timing

    def rules(self):
        return {
            "canteen_time": "1 PM",
            "exam_fee": self.exam_fee
        }


class Manasalu(School): # inheritance 

    def __init__(self, **kwargs):
        self.outing = kwargs.pop("outing",None)
        super().__init__(kwargs)

    def rules(self):
        parent_rules = super().rules()
        parent_rules.update({
            "school_time": "10PM"
        })
        return  parent_rules

manalu = Manasalu(holiday_timing="every friday and saturday", outing=True)
print(manalu.rules())

school = School(holiday_timing="hjhh")
print(school.outing)


"""
create a parent called Car. Implement a method called start_engine, 
shift_gare (can we create this method in Parent class or not), move_car
create and child called ElectricCar, DiselCar. 

if i call the start_car using electriCar object it should print "Start via electricity"
if i call the start_car uisng DisealCar it should print "Start via diseal"
if i call the shif_gare using ElectricCar it should print "Electric car dont have gare"


# variables 
Parent i.e. car should have a data like, brand_name (class variable) (this should be same across any object)
self_start (boolean_value), physical_key (it is only required in child class), oil_capacity 
(only available in child class)

"""

class Car():
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
 
    def start_engine(self):
        return("Vroom Vrrom")
 
    def shift_gear(self):
        return("Khachyaakk!!")
 
    def move_car(self):
        return ("Sararrarara")
 
 
class ElectricCar(Car):
    def __init__(self,brand,model,year,gear):
        super().__init__(brand,model,year)
        self.gear = gear
 
    def start_engine(self):
        return("jhuhjhujhujhujhuhju")
 
    def shift_gear(self):
        return("NO GEAR!!")
 
 
    def move_car(self):
        return("Moves with electricity!!")
       
 
class DieselCar(Car):
    def __init__(self,brand,model,year,gear):
        super().__init__(self,brand,model,year)
        self.gear = gear
 
    def start_engine(self):
        return("BRRRRRRRRRR")
   
    def shift_gear(self):
        return("6 gears")
 
    def move_car(self):
        return("Moves with Diesel")
 
run_Dieselcar = ElectricCar("Toyota","___","2020","6")
print(run_Dieselcar.shift_gear())
run_EVcar = ElectricCar("Tesla","X","2025","1000000kV")
print(run_EVcar.shift_gear())
 