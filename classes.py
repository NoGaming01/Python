"""All about classes ig"""

import time


class Car:
    """The Car Class"""

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.turned_on: bool = False

    def start(self) -> None:
        if self.turned_on:
            print("The car is running.")
        print(f"{self.name} is starting...")
        time.sleep(3)
        self.turned_on: bool = True
        print(f"{self.name} is started.")

    def drive(self) -> str:
        if not self.turned_on:
            return "The car isn't turned on."
        return f"You are driving {self.name}."
    
    def close(self) -> None:
        if not self.turned_on:
            print("The car isn't turned on.")
            return None
        self.turned_on: bool = False
        print(f"{self.name} is turned off.")


GTR: Car = Car("GTR")

GTR.start()
print(GTR.drive())
GTR.close()
