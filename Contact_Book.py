contacts = []
def add_contact():
    print("\n+================================+")
    print("|          Add Contact           |")
    print("+================================+")
    contact_id = input("Enter Contact ID: ")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contact = {
        "id": contact_id,
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact Added Successfully!")
def view_contact():
    print("\n+================================+")
    print("|          View Contact          |")
    print("+================================+")
    contact_id = input("Enter Contact ID: ")
    found = False
    for contact in contacts:
        if contact["id"] == contact_id:
            print("\nContact Details")
            print("--------------------------------")
            print(f"ID      : {contact['id']}")
            print(f"Name    : {contact['name']}")
            print(f"Phone   : {contact['phone']}")
            print(f"Email   : {contact['email']}")
            print(f"Address : {contact['address']}")
            print("--------------------------------")
            found = True
            break
    if not found:
        print("Contact Not Found!")
def search_contact():
    print("\n+================================+")
    print("|         Search Contact         |")
    print("+================================+")
    search = input("Enter Name or Phone Number: ").lower()
    found = False
    for contact in contacts:
        if (search in contact["name"].lower()
                or search in contact["phone"]):
            print("\nContact Found!")
            print("--------------------------------")
            print(f"ID      : {contact['id']}")
            print(f"Name    : {contact['name']}")
            print(f"Phone   : {contact['phone']}")
            print(f"Email   : {contact['email']}")
            print(f"Address : {contact['address']}")
            print("--------------------------------")
            found = True
    if not found:
        print("Contact Not Found!")
def edit_contact():
    print("\n+================================+")
    print("|          Edit Contact          |")
    print("+================================+")
    contact_id = input("Enter Contact ID: ")
    found = False
    for contact in contacts:
        if contact["id"] == contact_id:
            print("Contact Found!")
            contact["name"] = input("Enter New Name: ")
            contact["phone"] = input("Enter New Phone Number: ")
            contact["email"] = input("Enter New Email: ")
            contact["address"] = input("Enter New Address: ")
            print("Contact Updated Successfully!")
            found = True
            break
    if not found:
        print("Contact Not Found!")
def delete_contact():
    print("\n+================================+")
    print("|         Delete Contact         |")
    print("+================================+")
    contact_id = input("Enter Contact ID: ")
    found = False
    for contact in contacts:
        if contact["id"] == contact_id:
            contacts.remove(contact)
            print("Contact Deleted Successfully!")
            found = True
            break
    if not found:
        print("Contact Not Found!")
def view_all_contacts():
    print("\n+==============================================================+")
    print("|                    ALL CONTACTS                             |")
    print("+==============================================================+")
    if len(contacts) == 0:
        print("No Contacts Found.")
        return
    print(
        f"{'ID':<10}"
        f"{'Name':<20}"
        f"{'Phone':<15}"
        f"{'Email':<25}"
    )
    print("-" * 70)
    for contact in contacts:
        print(
            f"{contact['id']:<10}"
            f"{contact['name']:<20}"
            f"{contact['phone']:<15}"
            f"{contact['email']:<25}"
        )
    print("-" * 70)
    print(f"Total Contacts: {len(contacts)}")
while True:
    print("\n+================================+")
    print("|          Contact Book          |")
    print("+================================+")
    print("|  1. Add Contact                |")
    print("|  2. View Contact               |")
    print("|  3. Search Contact             |")
    print("|  4. Edit Contact               |")
    print("|  5. Delete Contact             |")
    print("|  6. View All Contacts           |")
    print("|  7. Exit                       |")
    print("+================================+")
    try:
        choice = int(
            input("Choose an Option From 1 To 7: ")
        )
        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contact()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            edit_contact()
        elif choice == 5:
            delete_contact()
        elif choice == 6:
            view_all_contacts()
        elif choice == 7:
            print("\n+================================+")
            print("|       Exited Successfully      |")
            print("+================================+")
            break
        else:
            print("Invalid Choice!")
            print("Please Choose Correct Choice!")
    except ValueError:
        print("Please Enter a Valid Number!")