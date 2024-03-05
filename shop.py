""" A Simple Shop."""

import random

class Customer:
    def __init__(self) -> None:
        self.get_information()

    def get_information(self) -> None:
        self.name: str = input("Name: ")
        self.age: str = input("Age: ")
        self.city: str = input("City: ")

    def __str__(self) -> str:
        return f"Customer is {self.name}, age is {self.age} and lives in {self.city}."

class Employee:
    def __init__(self) -> None:
        self.employees: list = ["Alice", "Bob", "Cathy", "Dan", "Eric"]
        self.branches: list = ["New York", "Los Angeles", "Chicago"]
        self.get_employee()

    def get_employee(self) -> None:
        self.employee: str = random.choice(self.employees)
        self.age: int = random.randint(18, 60)
        self.branch: str = random.choice(self.branches)

    def __str__(self) -> str:
        return f"Employee is {self.employee}, age is {self.age} and works in {self.branch} branch."
    
print(Customer())
print("-" * 20)
print(Employee())
