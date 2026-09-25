"""

Attribute of class and object

"""

class School:
    controlled_by = "PABSON" # class variable

    def __init__(self, name):
        self.name = name # instance variable

manasalu = School(name="Mansalu")
print(manasalu.controlled_by)
rising_star = School(name="Rising star")
print(rising_star.controlled_by)