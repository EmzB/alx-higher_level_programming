#!/usr/bin/python3

def inherits_from(obj, a_class):
    """ Return true if object is an inherited instance of a class.
        Else - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
