#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """ Return true if object is an instance or inherited instance of a class.
        Else - False  
        """
    if isinstance(obj, a_class):
        return True
    return False
