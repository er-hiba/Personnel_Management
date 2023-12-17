from Person import Person

class Employee(Person):
    _counter = 0

    def __init__(self, code, last_name, first_name, age, grade=10):
        super().__init__(code, last_name, first_name, age)
        self._grade = grade
        Employee._counter += 1

    def get_counter():
        return Employee._counter

    def get_grade(self):
        return self._grade

    def set_grade(self, g):
        self._grade = g

    def to_string(self):
        return f"Employee {self.get_code()}: {self.get_last_name()} {self.get_first_name()} - Age: {self.get_age()} - Grade: {self._grade}"
