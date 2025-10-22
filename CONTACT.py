def add_contact(contacts):
    """Adds a new contact to the contacts list."""
    name = input("Name: ")
    # Check if contact already exists
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(" Contact with this name already exists. Please use a unique name.")
            return

    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("✔ Contact added!")

def view_contacts(contacts):
    """Displays all contacts in a formatted list."""
    if not contacts:
        print(" No contacts found.")
    else:
        print("\n===== All Contacts =====")
        for c in sorted(contacts, key=lambda contact: contact["name"].lower()):
            print(f"Name: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}")
            print("-" * 25)

def search_contact(contacts):
    """Searches for a contact by name or phone number."""
    term = input("Enter name or phone to search: ")
    found = False
    for c in contacts:
        if term.lower() in c["name"].lower() or term in c["phone"]:
            print(f"\nName: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}")
            found = True
    if not found:
        print(" No records found.")

def update_contact(contacts):
    """Updates an existing contact's information."""
    term = input("Enter name or phone of contact to update: ")
    found = False
    for c in contacts:
        if term.lower() in c["name"].lower() or term in c["phone"]:
            print("Leave blank to keep current value.")
            c["name"] = input(f"New name (current: {c['name']}): ") or c["name"]
            c["phone"] = input(f"New phone (current: {c['phone']}): ") or c["phone"]
            c["email"] = input(f"New email (current: {c['email']}): ") or c["email"]
            c["address"] = input(f"New address (current: {c['address']}): ") or c["address"]
            print("✔ Contact updated!")
            found = True
            break
    if not found:
        print("⚠ No matching contact found.")

def delete_contact(contacts):
    """Deletes a contact by name or phone number."""
    term = input("Enter name or phone of contact to delete: ")
    found = False
    for i, c in enumerate(contacts):
        if term.lower() in c["name"].lower() or term in c["phone"]:
            confirm = input(f"Delete {c['name']}? (y/n): ")
            if confirm.lower() == 'y':
                contacts.pop(i)
                print(" Contact deleted!")
            else:
                print("Deletion cancelled.")
            found = True
            break
    if not found:
        print("⚠ No matching contact found.")

def main():
    """The main function to run the contact book application."""
    contacts = []
    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print(" Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()
