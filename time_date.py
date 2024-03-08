"""This is a playground to play with date and time."""

import datetime


now = datetime.datetime.now()

print(f"{now:%d.%m.%Y}")
print(f"{now:%D}")
print(f"{now:%d-%B-%Y}")
print(f"{now:%H:%M}")
