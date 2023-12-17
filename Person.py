from abc import ABCMeta, abstractmethod

class Person(metaclass=ABCMeta):
    _counter = 0   
    
    def __init__(self, code=100, last_name="Erraoui", first_name="Hiba", age="19"):
        self._code = code
        self._last_name = last_name
        self._first_name = first_name
        self._age = age
        Person._counter += 1

    @classmethod
    def get_counter(cls):
        return Person._counter

    def get_code(self):
        return self._code

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_age(self):
        return self._age

    def set_code(self, c):
        self._code = c

    def set_last_name(self, n):
        self._last_name = n

    def set_first_name(self, p):
        self._first_name = p

    def set_age(self, a):
        self._age = a

    @abstractmethod
    def to_string(self):
        pass     

    def equals(self, other):
        return self._code == other._code
