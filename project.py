import re
import os
from tabulate import tabulate
import csv

def main():
    while True:
        stage1()

def stage1():
    clear_screen()
    print("\n\n=== EcoCredit Waste Management System ===")
    print("\n\t1. Login")
    print("\t2. Create Account")
    print("\t3. Exit")
    choice = input("\nEnter your choice: ")
    if choice == "1":
        login()
    elif choice == "2":
        create_account()
    elif choice == "3":
        clear_screen()
        print("Thank you for using EcoCredit")
        exit()
    else:
        print("Invalid choice")

def clear_screen():
    os.system("clear")

def create_account():
    clear_screen()
    username = create_username()
    password = create_password()
    save_user(username, password)
    frame2(username)

def create_username():
    while True:
        clear_screen()
        print("\n=== EcoCredit Waste Management System ===\n")
        username = input("Enter username: ")
        if username.strip() == "":
            print("Username cannot be empty")
            continue
        try:
            with open("users.csv") as file:
                for line in file:
                    row = line.rstrip().split(",")
                    if username == row[0]:
                        print("\n=== EcoCredit Waste Management System ===\n")
                        print("Username already exists")
                        break
                else:
                    return username
        except FileNotFoundError:
            print("users.csv file not found")

def validate_password(password):
    if len(password) < 8:
        return False, "Too short"
    if not re.search(r"[A-Z]", password):
        return False, "Need an uppercase letter"
    if not re.search(r"[a-z]", password):
        return False, "Need a lowercase letter"
    if not re.search(r"\d", password):
        return False, "Need a number"
    if not re.search(r"[@$!%*?&]", password):
        return False, "Need a special character"
    return True, "Strong password"


def create_password():
    while True:
        clear_screen()
        print("\n=== EcoCredit Waste Management System ===\n")
        password = input("Enter strong password: ")
        valid, message = validate_password(password)
        if valid:
            print("\n=== EcoCredit Waste Management System ===\n")
            print("Password accepted")
            return password
        else:
            print("\n=== EcoCredit Waste Management System ===\n")
            print("Weak password")
            print(message)
            print("\nPassword must contain:")
            print("- Uppercase letter")
            print("- Lowercase letter")
            print("- Number")
            print("- Special character")
            print("- Minimum 8 characters")

def save_user(username, password):
    try:
        with open("users.csv", "a") as file:
            file.write(f"{username},{password},0\n")
        print("Account created successfully!")
    except FileNotFoundError:
        print("users.csv file not found")

def login():
    clear_screen()
    username = check_username()
    password = check_password(username)
    frame2(username)

def check_username():
    attempts = 3
    while attempts > 0:
        clear_screen()
        print(f"Attempts left: {attempts}")
        username = input("Enter username: ")
        if username.strip() == "":
            print("Username cannot be empty")
            continue
        try:
            with open("users.csv") as file:
                for line in file:
                    row = line.rstrip().split(",")
                    if username == row[0]:
                        return username
            attempts -= 1
            print("Username not found")
        except FileNotFoundError:
            print("users.csv file not found")
    clear_screen()
    stage1()

def check_password(username):
    attempts = 3
    while attempts > 0:
        clear_screen()
        print(f"Attempts left: {attempts}")
        password = input("Enter password: ")
        if password.strip() == "":
            print("Password cannot be empty")
            continue
        try:
            with open("users.csv") as file:
                for line in file:
                    row = line.rstrip().split(",")
                    if username == row[0] and password == row[1]:
                        return password
            attempts -= 1
            print("Invalid password")
        except FileNotFoundError:
            print("users.csv file not found")
    clear_screen()
    stage1()

def frame2(username):
    while True:
        clear_screen()
        print("\n=== EcoCredit Waste Management System ===\n")
        print(f"=== {username} login successful ===")
        print("\n\t1. Deposit Waste")
        print("\t2. Check Credit score")
        print("\t3. Logout")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            deposit_waste(username)
        elif choice == "2":
            check_credit(username)
        elif choice == "3":
            clear_screen()
            return
        else:
            print("Invalid choice")

def deposit_waste(username):
    while True:
        clear_screen()
        try:
            with open("data/waste_data.csv") as file:
                reader = csv.reader(file)
                data = list(reader)
        except FileNotFoundError:
            print("waste_data.csv file not found")
            return
        print(tabulate(data, headers="firstrow", tablefmt="grid"))
        waste_code = input("\nEnter item code: ")
        if waste_code.strip() == "":
            print("Item code cannot be empty")
            continue
        try:
            waste_weight = int(input("Enter weight in grams: "))
            if not valid_weight(waste_weight) or waste_weight > 3000:
                print("User needs to deposit up to 3kg per item")
                continue
        except ValueError:
            print("Enter valid number")
            continue
        for row in data[1:]:
            if waste_code.strip() == row[0].strip():
                credit_per_gram = int(row[3])
                total_credit = calculate_credit(waste_weight, credit_per_gram)
                update_credit(username, total_credit)
                print(f"\n{total_credit} credits added successfully!")
                break
        else:
            print("Invalid item code")
        while True:
            print("\n1. Enter Again")
            print("2. Check Credit Score")
            print("3. Logout")
            choice = input("\nEnter your choice: ")
            if choice == "1":
                break
            elif choice == "2":
                check_credit(username)
            elif choice == "3":
                return
            else:
                print("Invalid choice")

def calculate_credit(weight, credit_per_gram):
    return weight * credit_per_gram
def valid_weight(weight):
    return weight > 0

def update_credit(username, total_credit):
    rows = []
    try:
        with open("users.csv") as file:
            reader = csv.reader(file)
            header = next(reader)
            rows.append(header)
            for row in reader:
                if row[0] == username:
                    try:
                        row[2] = str(int(row[2]) + total_credit)
                    except ValueError:
                        row[2] = str(total_credit)
                rows.append(row)
    except FileNotFoundError:
        print("users.csv file not found")
        return
    with open("users.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def check_credit(username):
    clear_screen()
    try:
        with open("users.csv") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if username == row[0]:
                    print(f"\nYour current credits: {row[2]}")
                    input("\nPress Enter to continue...")
                    clear_screen()
                    break
    except FileNotFoundError:
        print("users.csv file not found")

if __name__ == "__main__":
    main()
