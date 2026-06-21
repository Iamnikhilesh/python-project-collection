# Contact Book
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} - {self.phone}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, search_query):
        found_contacts = [contact for contact in self.contacts if
                          search_query.lower() in contact.name.lower() or search_query in contact.phone]
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print("No contacts found.")

    def update_contact(self, search_query):
        found_contacts = [contact for contact in self.contacts if
                          search_query.lower() in contact.name.lower() or search_query in contact.phone]
        if found_contacts:
            selected_contact = found_contacts[0]
            print(f"Updating contact: {selected_contact.name}")
            selected_contact.name = input("Enter new name: ")
            selected_contact.phone = input("Enter new phone number: ")
            selected_contact.email = input("Enter new email: ")
            selected_contact.address = input("Enter new address: ")
            print("Contact updated successfully!")
        else:
            print("No contacts found.")

    def delete_contact(self, search_query):
        found_contacts = [contact for contact in self.contacts if
                          search_query.lower() in contact.name.lower() or search_query in contact.phone]
        if found_contacts:
            confirmed = input(f"Do you want to delete {found_contacts[0].name} - {found_contacts[0].phone}? (yes/no): ")
            if confirmed.lower() == "yes":
                self.contacts.remove(found_contacts[0])
                print("Contact deleted successfully!")
        else:
            print("No contacts found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_manager.add_contact(contact)

        elif choice == "2":
            contact_manager.view_contacts()

        elif choice == "3":
            search_query = input("Enter name or phone number to search: ")
            contact_manager.search_contact(search_query)

        elif choice == "4":
            search_query = input("Enter name or phone number to update: ")
            contact_manager.update_contact(search_query)

        elif choice == "5":
            search_query = input("Enter name or phone number to delete: ")
            contact_manager.delete_contact(search_query)

        elif choice == "6":
            print("Exiting Contact Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
