import json
import os

def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def display_menu():
    print("\nContact Management System")
    print("1. Add a new contact")
    print("2. View contact list")
    print("3. Edit a contact")
    print("4. Delete a contact")
    print("5. Exit")

def add_contact(contacts):
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for name, info in contacts.items():
            print(f"{name}: {info['phone']}, {info['email']}")

def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ")
    
    if name in contacts:
        print(f"Editing contact '{name}':")
        new_phone = input("Enter the new phone number (press enter to keep the current): ")
        new_email = input("Enter the new email address (press enter to keep the current): ")

        if new_phone:
            contacts[name]['phone'] = new_phone
        if new_email:
            contacts[name]['email'] = new_email

        print(f"Contact '{name}' edited successfully.")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")

    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

if __name__ == "__main__":
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
