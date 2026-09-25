class School:

    def __init__(self, name, estd_date, rules, fee):
        """ to store the data in computer memory"""
        self.name = name
        self.estd_date = estd_date
        self.rules = rules
        self.fee = fee
        self.canteen_food = {
                "rice": 2000
            }

    def assembly(self):
        pass

    def cook_food(self, vegetables):
       print(vegetables, self.canteen_food)


kmc_school = School(name="KMC", estd_date=1990, rules={}, fee=40000)
kmc_school.takes_outing = True
kmc_school.cook_food({
    "potato": "1kg",
    "ginger": 200
})

rato_bangla = School(name="Rato bangla", estd_date=1990, rules={}, fee=100000)
rato_bangla.takes_outing = False
rato_bangla.assembly()


print(kmc_school.name)
print(kmc_school.takes_outing)
print(rato_bangla.name)
print(rato_bangla.takes_outing)



"""
Creat a class called Move that will accept name, actors, actress, price, producer.
It should have a method called display_information()
"""