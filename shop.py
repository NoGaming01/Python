"""A Simple Shop Game"""

import random
import uuid
import os

os.system("cls" if os.name == "nt" else "clear")

uid = uuid.uuid4()

class Shop:
    def __init__(self, name="The Shop"):
        self.name = name
        self.data = {}

    def welcome(self):
        pass

    def store_data(self, key, value):
        self.data[key] = value
    
class Customer(Shop):
    def __init__(self):
        super().__init__()
        self.get_information()

    def get_information(self):
        self.name = str(input("What is your name? ")).capitalize().strip()
        self.age = int(input("What is your age? "))
        self.city = str(input("What is your city name? ")).capitalize().strip()

    def store_data(self):
        serial_number = len(self.data) + 1

        key = f"customer-{serial_number}"

        data = {
            "name": self.name,
            "age": self.age,
            "city": self.city,
            "id": uid
        }

        super().store_data(key, data)
        print(self.data)

class Employee(Shop):
        def __init__(self):
            super().__init__()
            self.employees = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"]

        def get_employee(self):
            pass
           
customer = Customer()

customer.store_data()
