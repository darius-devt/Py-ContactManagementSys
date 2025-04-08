# 1. Create a class named Contacts with the following attributes:
#    - name
#    - phone_number
#    - email

class Contacts:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Contact Name: {self.name}, Phone Number: {self.phone_number}, Email: {self.email}"