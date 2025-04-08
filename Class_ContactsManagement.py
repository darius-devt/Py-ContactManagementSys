# 2. Create a class ContactsManagement that contains a list of contacts and methods to:
# - add,
# - show,
# - search,
# - and delete contacts.
import os

class ContactsManagement:
    filename = "ContactList.txt"  # Default filename for the contact list

    def __init__(self):
        self.contacts = []  # Initialize an empty list to store contacts
        if os.path.isfile(self.filename):
            self.show_contacts()  # Just display the contacts
        else:
            self.create_file()

    def create_file(self):
        with open(self.filename, 'w', encoding="utf8") as file:
            pass  # Create an empty file
    
    def add_contact(self, name, phone_number, email):
        with open(self.filename, 'a', encoding="utf8") as file:
            file.write(f"{name} | {phone_number} | {email}\n")

    def show_contacts(self):
        with open(self.filename, "r", encoding="utf8") as file:
            print("- Contacts List: -")
            print(file.read())

    def search_contact(self, name):
        try:
            with open(self.filename, "r", encoding="utf8") as file:
                contacts = file.readlines()
                found = False
                for contact in contacts:
                    if name.lower() in contact.lower():     # Checks if the name (converted to lowercase) is a substring of the contact (also converted to lowercase).
                        found = True
                        contact_details = contact.strip().split(" | ")     
                        print(f"Contact Found: Name: {contact_details[0]}, Phone Number: {contact_details[1]}, Email: {contact_details[2]}")
                if not found:
                    print(f"Contact {name} not found in {self.filename}.")
        except FileNotFoundError:
            print(f"File {self.filename} not found.")

    def delete_contact(self, name):
        try:
            with open(self.filename, 'r', encoding="utf8") as file:
                contacts = file.readlines()
                if not contacts:
                    print("No contacts to delete.")
                    return
            
            with open(self.filename, 'w', encoding="utf8") as file:
                contact_deleted = False
                for contact in contacts:
                    if name.lower() not in contact.lower():  # Case-insensitive check
                        file.write(contact)
                    else:
                        contact_deleted = True
                
                if contact_deleted:
                    print(f"Contact '{name}' deleted successfully.")
                else:
                    print(f"Contact '{name}' not found.")
        except FileNotFoundError:
            print(f"File {self.filename} not found.")