'''
CS 115, Lab 12, Inheritance

Author: Jun Hong Wang
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 1 
' Implement missing sections of the Car class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Car(object):
    '''Write the constructor. It should take in four arguments:
       - make (a string, the company name, a.k.a. brand)
       - model (a string)
       - mpg (miles per gallon, a float)
       - tank_capacity (capacity of the gas tank in gallons, a float)
       These should all be assigned to corresponding private fields, i.e., with
       names that start with '__'.  Use the names in the 'str' method provided below.
       '''
    def __init__(self, make, model, mpg, tank_capacity):
        """
        sets instance variables to variables given in constructor
        """
        self.__make = make
        self.__model = model
        self.__mpg = mpg
        self.__tank_capacity = tank_capacity

    '''Write getters for make, model, mpg, and tank_capacity.'''
    def get_make(self):
        """
        sets make
        """
        return self.__make
    
    def get_model(self):
        """
        sets model
        """
        return self.__model
    
    def get_mpg(self):
        """
        sets mpg
        """
        return self.__mpg
    
    def get_tank_capacity(self):
        """
        sets tank capacity
        """
        return self.__tank_capacity

    '''Write setters for mpg and tank_capacity.'''
    def set_mpg(self, new_mpg):
        """
        sets mpg
        """
        self.__mpg = new_mpg

    def set_tank_capacity(self, new_capacity):
        """
        sets tank capacity
        """
        self.__tank_capacity = new_capacity 

    '''Write a method called get_total_range.
       It returns the total distance the car can travel on a full tank of
       gas.'''
    def get_total_range(self):
        """
        multiplies miles per gallon by capacity (gallons)
        """
        return self.__mpg * self.__tank_capacity

    def __str__(self):
        '''A string for printing information about a car.'''
        return self.__make + ' ' + self.__model + ', MPG: ' + str(self.__mpg) \
            + ', tank capacity: ' + str(self.__tank_capacity)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 2 
' Implement missing sections of the HybridCar class. 
' Make HybridCar be a subclass of Car.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class HybridCar(Car):  
    '''Write the constructor. It should take in 6 arguments:
    - the first four are the same as in the Car constructor
    - battery_kWh (battery power in kilowatt-hours, a float)
    - miles_per_kWh (miles per kilowatt-hours, a float)
    The additional fields must be private.
    '''
    def __init__(self, make, model, mpg, tank_capacity, battery_kWh, miles_per_kWh):
        """
        calls constructor of car, passing in self
        sets new instance variables
        """
        Car.__init__(self, make, model, mpg, tank_capacity)
        self.__battery_kWh = battery_kWh
        self.__miles_per_kWh = miles_per_kWh

    '''Implement the following method.'''
    def get_battery_range(self):
        '''Returns the total distance the car can travel on a fully charged
        battery.
        '''
        return self.__battery_kWh * self.__miles_per_kWh
 

    '''Override the method get_total_range.
    Returns the total distance the car can travel on a full tank of
    gas and a fully charged battery.
    Do not do any math here except a single +. To get credit, you must call
    the methods you have already written.
    '''
    def get_total_range(self):
        """
        uses total range function from superclass, passing in self + battery range function in this class
        """
        return Car.get_total_range(self) + self.get_battery_range()

    def __str__(self):
        '''A string for printing information about a car.'''
        return super().__str__() + ', battery kWh: ' + \
            str(self.__battery_kWh) + ', miles/kWh: ' + \
            str(self.__miles_per_kWh)

# hc = HybridCar("Toyota", "Prius", 20.0, 25.0, 10.0, 10.0)
# print(hc)