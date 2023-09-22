import csv


column_names = ["EMAIL", "MOBILE NUMBER", "USERNAME", "PASSWORD"]

def create_csv_file():
    
    csv_file = "user_data.csv"

    
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(column_names)

def register_user(email, mobile_number, username, password):
    
    csv_file = "user_data.csv"

    
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)

      
        writer.writerow([email, mobile_number, username, password])

def login_user(username, password):
    
    csv_file = "user_data.csv"

    
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            saved_username, saved_password = row[2], row[3]  
            if username == saved_username and password == saved_password:
                return True

    return False

def main():
    
    create_csv_file()

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            
            email = input("Enter Email: ")
            mobile_number = input("Enter Mobile Number: ")
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            
            
            register_user(email, mobile_number, username, password)
            print("User registered successfully!")
        
        elif choice == '2':
            
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            
            
            if login_user(username, password):
                print("Login successful!")
            else:
                print("Login failed. Invalid username or password.")
        
        elif choice == '3':
            break

if __name__ == "__main__":
    main()
