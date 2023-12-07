"""
umbrella class of Object
don't need to explicitly call __init__ function, it just does it automatically

instance vars defined as private (so __ in front)
there are also reserved comparison methods for objects
    but these need to be written for each object in order to have a good comparison method
    __ge__ is greater than or equal to, 
    __eq__ is equals to, etc...
    interpreter doesn't check for how the method is implemented, other than it being valid syntax
"""

