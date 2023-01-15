#!/usr/bin/python3

def is_same_class(obj, a_class):
    """ Returns true if an object is an instance of a specified class.
        Else - False.
    """
    if type(obj) == a_class:
        return True
    return False
