#!/usr/bin/python3
"""json"""


class Student:
    """A student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance."""
        if attrs is not None and all(isinstance(x, str) for x in attrs):
            d = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    d[k] = v
            return d
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """reload data from json"""
        for (key, value) in json.items():
            setattr(self, key, value)[A[A[A[A[A[A[A[A[A[A[A[A[A[A[A[A[A[A[A[A[A[A[A[A[A[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[creating class Student"""[B[B[B[B[B[B[B[B[B[B[B[B[B[B[B[B[B[[C[C[C[C[C[C[C[C[C[C[C[C[C[C[Celoading data"""[A[A[A[A[A[A[A[A[A[A[A[A[B[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[class instance[C[C[C[C[[C[C"""[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D """Getting a dic[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[Cthe[C[C[C[C[C[C obj instance[D[D[D[D[D[D[D[Dthe insta[B[B[B[B[B[B[B[B[B[B[B[B[B[B[B[B[B


