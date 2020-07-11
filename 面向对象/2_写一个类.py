# -*- coding: utf-8 -*-

class Car():
    def __init__(self,name,price):
        self.name = name
        self.price = price
        #默认属性
        self.meter = 0
    def get_price(self):
        return self.price
    
    
my_car = Car("bmw",12000)
print(my_car.name)
print(my_car.price)

price = my_car.get_price()
print(price)

print(my_car.meter)













