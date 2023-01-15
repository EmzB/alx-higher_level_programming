#!/usr/bin/python3
"""
New class that inherits from list object
"""


class MyList(list):
    
    def print_sorted(self):
        """
        prints a list in ascending order 
        """
        print(sorted(self))
