import json
import os


contacts = []

if os.path.exists("contact.json"):
    with open("contact.json","r") as f:
        contacts = json.load(f)


def save_contacts():
    with open("contacts.josn","w") as f :
        json.dump(contacts, f)


while True:
    print("\n📒Contact Book Menu: ")
    print("1. Add new contact")
    print("2. Show all contact")
    print("3. Search contact by name")
    print("4. Edit contact")
    print("5. Delet contact")
    print("6. Exit")
    
    choice = input("Choice an option(1-6): ")
    if choice == "1":
        print(">> Add a New Contact")
        name =input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email adderss: ")

        contact = {
            "name" : name,
            "phone":phone,
            "email":email
        }
        contacts.append(contact)
        save_contacts()
        print(f"✅ Contact '{name}' added successfully.")

    elif choice == "2":
        if not contacts:
            print("📭 No contacts found.")
        else:
            print("📇 All Contacts: ")
            for i, c in enumerate(contacts, 1):
                print(f"{i}. Name:{c['name']},Phone:{c["phone"]}, Email:{c["email"]}")    

    elif choice == "3":
          search_name = input("🔍 Enter name to search: ").lower()
          found = False  
          for c in contacts:
              if c['name'].lower() == search_name:
                  print(f"✅ Found: Name : {c['name']},Phone : {c['phone']}, Email: {c['email']}")
                  found = True
                  break
          if not found:
              print("❌ Contact not found.")  



    elif choice == "4":
        edit_name = input("Enter the name of contact to edit: ").lower()
        for c in contacts:
            if c["name"].lower() == edit_name:
                new_name = input("Enter new name: ")
                new_phone = input("Enter new phone number: ")
                new_email = input("Enter new email address: ")
                c["name"] = new_name
                c["phone"] = new_phone
                c["email"] = new_email
                save_contacts()
                print("Contact updated successfuly!")
                break
            
            else:
                print("Coontact not found!.")


    elif choice == "5":
        delete_name = input("Enter the name of the contact to delete: ").lower()
        for i , c in enumerate(contacts):
            if c["name"].lowe() == delete_name:
                remowed = contacts.pop(i)
                save_contacts()
                print(f"Contact '{remowed['name']}' delete successfuly!")
            else:
                print("Contact not found")    


    elif choice == "6":
        break
    
    else:
        print("Invalid choice.!") 