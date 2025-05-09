users = {}  # Dictionary to store username and password

def register():
    username = input("Enter a username: ")
    if username in users:
        print("User already exists!")
    else:
        password = input("Enter a password: ")
        users[username] = password
        print("User registered successfully!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Login failed!")

# Menu
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exit!")
        break
    else:
        print("Invalid option.")
