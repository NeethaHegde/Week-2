users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

def add_user():
    id = int(input("Enter new user ID: "))
    name = input("Enter name: ")
    email = input("Enter email: ")
    users.append({"id": id, "name": name, "email": email})
    print("User added.\n")

def get_user():
    id = int(input("Enter user ID to retrieve: "))
    for user in users:
        if user["id"] == id:
            print("User found:", user, "\n")
            return
    print("User not found.\n")

def update_user():
    id = int(input("Enter user ID to update: "))
    for user in users:
        if user["id"] == id:
            name = input("Enter new name (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            if name:
                user["name"] = name
            if email:
                user["email"] = email
            print("User updated.\n")
            return
    print("User not found.\n")

def delete_user():
    id = int(input("Enter user ID to delete: "))
    global users
    users = [user for user in users if user["id"] != id]
    print("User deleted (if existed).\n")

def list_users():
    print("All users:")
    for user in users:
        print(user)
    print()

while True:
    print("CRUD MENU")
    print("1. Add User")
    print("2. Get User by ID")
    print("3. Update User")
    print("4. Delete User")
    print("5. List All Users")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_user()
    elif choice == "2":
        get_user()
    elif choice == "3":
        update_user()
    elif choice == "4":
        delete_user()
    elif choice == "5":
        list_users()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option.\n")
