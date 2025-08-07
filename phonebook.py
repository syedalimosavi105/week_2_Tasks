import json
import os

FILENAME = 'contacts.json'

# Load contacts from file if it exists
if os.path.exists(FILENAME):
    with open(FILENAME, 'r') as f:
        contacts = json.load(f)
else:
    contacts = {}

def save_contacts():
    with open(FILENAME, 'w') as f:
        json.dump(contacts, f)
    print("Contacts saved.\n")

def create_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact added.\n")

def read_contact():
    name = input("Enter contact name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}\n")
    else:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter contact name to update: ")
    if name in contacts:
        new_phone = input("Enter new phone number: ")
        contacts[name] = new_phone
        print("Contact updated.\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter contact name to delete: ")
    if contacts.pop(name, None):
        print("Contact deleted.\n")
    else:
        print("Contact not found.\n")

def list_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("All Contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
        print()

# CLI Menu Loop
while True:
    print("Phonebook Menu:")
    print("1) Create  2) Read  3) Update  4) Delete  5) List  6) Save  7) Exit")
    choice = input("Select option: ")
    if choice == '1':
        create_contact()
    elif choice == '2':
        read_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        list_contacts()
    elif choice == '6':
        save_contacts()
    elif choice == '7':
        save_contacts()
        print("Goodbye!")
        break
    else:
        print("Invalid choice.\n")