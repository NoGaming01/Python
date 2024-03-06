"""A Simple Shop Game"""

import random
import uuid

class Shop:
    def __init__(self, name="The Shop"):
        self.name = name
        self.data = {}

    def __str__(self):
        return self.name
    
class Customer(Shop):
    def __init__(self):
        super().__init__()

    def get_information(self):
        self.name = str(input("What is your name? ")).capitalize().strip()
        self.age = int(input("What is your age? ")).strip()
        self.city = str(input("What is your city name? ")).capitalize().strip()

    def store_data(self):
        serial_number = len(self.data) + 1

        key = f"customer-{serial_number}"

        self.data[key] = {}

        print("Added the data.")
        print(self.data)
        
customer = Customer()

customer.store_data()
