#Ntombekazi Sibetyu Car classes

#imorting the cars dictionary from the car_data ffile
from car_data import cars,get_cars_based_on_make
import math

#importing datetime module to be able to get time
import datetime

#gettinf the current date
current_date = datetime.datetime.now()

#parent class for the classes w
class Cars:

    #initialising the properties of the car class whic are also the properties of the cars
    def __init__(self,car_id,year_model,distance_driven,base_price,tank_size,kilometers_per_tank,make):
        self.car_id = car_id
        self.year_model = year_model
        self.distance_driven = distance_driven
        self.base_price = base_price
        self.tank_size = tank_size
        self.kilometers_per_tank = kilometers_per_tank
        self.make = make

    def __str__(self):
        return "Car id %s, \nyear model %s, \ndistance driven %s, \nbase price %s, \ntank size %s, \nkilometers per tank %s, \nmake %s, "%(self.car_id,self.year_model,self.distance_driven,self.base_price,self.tank_size,self.kilometers_per_tank,self.make)

    #defining a function that calculates the fuel usage of a car
    def fuel_usage(self):
        return self.kilometers_per_tank/self.tank_size

    #defining a function that calculates the resell value of a car depending on the years the car has
    def resell_value(self):

        #calculting the years the car has using the current date minus the cars year model
        car_age = int(current_date.strftime("%Y")) - self.year_model
        times = int(0.9)

        if car_age < 20:
            return self.base_price*(times^car_age)

        if car_age >= 20:

            return self.base_price*(times^car_age) + 20000

car_1 = Cars(1,1995,240000,200000,30,100,"Volkswagen")
car_2 = Cars(2,2010,10000,300000,20,120,"Volkswagen")
car_3 = Cars(3,2017,300000,900000,15,80,"Volkswagen")
car_4 = Cars(4,1982,560000,50000,25,150,"Mercedes")
car_5 = Cars(5,2012,30000,500000,20,90,"Mercedes")
car_6 = Cars(6,2019,10000,1000000,15,100,"Mercedes")
car_7 = Cars(7,2000,600000,250000,25,200,"Toyota")
car_8 = Cars(8,2015,30000,350000,20,100,"Toyota")
car_9 = Cars(9,2018,2000,800000,25,200,"Toyota")

print(car_4)
car_5.fuel_usage()

#child class for totta cars
class Toyota(Cars):

    def __init__(self):
        pass

    #function that gets toyota cars from the dictionary
    def get_toyota_cars(self):
        return get_cars_based_on_make("Toyota")


    def __str__(self):
        return "The resell value is %s and the fuel usage is $s"%(self.resell_value(),self.fuel_usage())

toyota_car = Toyota(Cars)
toyota_car.get_toyota_cars()

#second child class
class Mercedes(Cars):

    def __init__(self):
        pass

    def get_mercedes_cars(self):
        get_cars_based_on_make("Mercedes")

    def __str__(self):
        return "The resell value is %s and the fuel usage is $s"%(self.resell_value(),self.fuel_usage())

a_car = Mercedes(Cars)
mercedes_car = a_car.get_mercedes_cars()
Mercedes(Cars)

class Volkswagen(Cars):

    def __init__(self):
        pass

    def vw_cars(self):
        get_cars_based_on_make("Volkswagen")

    def __str__(self):
        return "The resell value is %s and the fuel usage is $s"%(self.resell_value(),self.fuel_usage())

vw_car = Volkswagen(Cars)






