# 3. Implement a menu that allows the user to select an action:
# - add,
# - show,
# - search,
# - or delete a contact,
# - and exit the program.

from Class_ContactsManagement import ContactsManagement
from Class_Contacts import Contacts

class ContactsManagementSystem:

    def __init__(self):
        self.ContactsManagement = ContactsManagement()

    def contacts_menu(self):
        exit = False
        print('*** Contacts Management System Menu ***')
        self.ContactsManagement.show_contacts()
        while not exit:
            try:
                option = self.display_menu()
                exit = self.execute_option(option)
            except Exception as e:
                print(f'Error: {e}')

    def display_menu(self):
        print('''- Contacts Management System Menu -"
        1. Add Contact
        2. Show Contacts
        3. Search Contact
        4. Delete Contact
        5. Exit''')
        return int(input("Select an option (1-5): "))

    def execute_option(self, option):
        if option == 1:
            contact = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            new_contact = Contacts(contact, phone_number, email)
            self.ContactsManagement.add_contact(new_contact.name, new_contact.phone_number, new_contact.email)
            print(f"Contact '{new_contact.name}' added successfully.")
        elif option == 2:
            self.ContactsManagement.show_contacts()
        elif option == 3:
            contact = input("Enter contact name to search: ")
            self.ContactsManagement.search_contact(contact)
        elif option == 4:
            contact = input("Enter contact name to delete: ")
            self.ContactsManagement.delete_contact(contact)
        elif option == 5:
            print("Exiting the program...")
            return True
        else:
            print("Invalid option, please choose a number between 1 and 5.")
            return False

if __name__ == '__main__':
    app = ContactsManagementSystem()
    app.contacts_menu()