from Person import Person
from Employee import Employee
from Student import Student

# Creating an Employee
emp1 = Employee(code=101, last_name="ERRAOUI", first_name="Hiba", age="30", grade=8)
emp2 = Employee(code=102, last_name="ESSADAQ", first_name="Aabla", age="35", grade=9)

# Creating a Student
student1 = Student(code=201, last_name="ERRAOUI", first_name="Hiba", age="20", level="2nd year", average=17)
student2 = Student(code=202, last_name="ESSADAQ", first_name="Aabla", age="21", level="3rd year", average=17)

# Printing information about employees and students
print("--- Employees ---")
print(emp1.to_string())
print(emp2.to_string())

print("\n--- Students ---")
print(student1.to_string())
print(student2.to_string())

# Getting the total count of Persons, Employees, and Students
print("\nTotal count of Persons:", Person.get_counter())
print("Total count of Employees:", Employee.get_counter())
print("Total count of Students:", Student.get_counter())

