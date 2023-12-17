from Person import Person

class Student(Person):
    _counter = 0

    def __init__(self, code, last_name, first_name, age, level="1st year", average=18):
        super().__init__(code, last_name, first_name, age)
        self._level = level
        self._average = average
        Student._counter += 1

    def get_counter():
        return Student._counter

    def get_level(self):
        return self._level

    def get_average(self):
        return self._average

    def set_level(self, n):
        self._level = n

    def set_average(self, m):
        self._average = m

    def to_string(self):
        return f"Student {self.get_code()}: {self.get_last_name()} {self.get_first_name()} - Age: {self.get_age()} - Level: {self._level} - Average: {self._average}"

