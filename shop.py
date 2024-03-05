""" A Simple Shop."""

import random

employees: list = ["Alice", "Bob", "Cathy", "Dan", "Eric"]
products: list = ["milk", "eggs", "bread", "cheese", "apples", "oranges"]

def check_product(product: str):
    if product.lower() in products:
        return True
    else:
        return False
    
def get_employee():
    return random.choice(employees)

def bill(customer_name: str, product: str, employee: str):
    print("-" * 20)
    print(f"Name: {customer_name}")
    print(f"Product: {product}")
    print(f"Employee: {employee}")

customer_name: str = input("Name: ")

while True:
    product: str = input("Product: ")
    employee: str = get_employee()

    if check_product(product):
        bill(customer_name, product, employee)
        break
    else:
        print(f"{product} is not available")
