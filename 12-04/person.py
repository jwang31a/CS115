class Person:
    def __init__(self, first, last):
        self.firstName = first
        self.lastName = last
    
    def asleep(self, time):
        return 0 <= time <= 7
    
    def __str__(self):
        return self.firstName + " " + self.lastName
    
"""
like class Student extends Person
"""
class Student(Person):
    def __init__(self, first, last, Id):
        Person.__init__(self, first, last)
        self.ID = Id

    def asleep(self, time):