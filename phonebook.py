"""
Challenge: Phonebook App

Write a Python program to implement a phonebook app that allows users to add, delete, and search for contacts. The app should use a dictionary to store contact information, with the contact name as the key and the phone number as the value.
The app should have the following features:
- Add a contact: Prompt the user to enter a contact name and phone number, then add the contact to the dictionary. If the contact already exists, display an error message and do not add the contact.
- Delete a contact: Prompt the user to enter a contact name, then delete the contact from the dictionary if it exists. If the contact does not exist, display an error message.
- Search for a contact: Prompt the user to enter a contact name, then display the contact's phone number if it exists. If the contact does not exist, display an error message.
- Print all contacts: Display all contacts and their phone numbers in the dictionary.
"""

phonebook = {}

def add_contact():
    """Add a contact to the phonebook."""
    name = input("Enter a name: ")
    number = input("Enter a number: ")
    if name in phonebook:
        print("Contact already exists.")
    else:
        phonebook[name] = number
        print("Contact added.")
        
def delete_contact():
    """Delete a contact from the phonebook."""
    name = input("Enter a name: ")
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")
        
def search_contact():
    """Search for a contact in the phonebook."""
    name = input("Enter a name: ")
    if name in phonebook:
        print(phonebook[name])
    else:
        print("Contact not found.")
        
def print_contacts():
    """Print all contacts in the phonebook."""
    for name, number in phonebook.items():
        print(name, number)
