import datetime
import time
import math
import random
import uuid


print("---------------------------------------------------")
print(" WELCOME TO MULTI-UTILITY TOOL KIT")
print("---------------------------------------------------")
def create_file(filename):
    with open(filename, "w") as f:
        pass
    print("File created successfully!")

def write_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)
    print("Data written successfully!")

def read_file(filename):
    try:
        with open(filename, "r") as f:
            print("\nFile Content:")
            print(f.read())
    except FileNotFoundError:
        print("File not found!")

def append_file(filename, data):
    with open(filename, "a") as f:
        f.write("\n" + data)
    print("Data appended successfully!")



#  (CUSTOM FUNCTIONS)

def circle_area(r):
    return math.pi * r * r

def km_to_m(km):
    return km * 1000



# DATETIME MENU

def datetime_menu():
    while True:
        print("\nDatetime Menu")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main menu")
        ch = input("Choose: ")

        if ch == "1":
            print("Current Date & Time:", datetime.datetime.now())

        elif ch == "2":
            print("Enter date in YYYY-MM-DD format only")
            d1 = input("Enter first date: ")
            d2 = input("Enter second date: ")

            try:
                date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
                date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
            except ValueError:
                print("Please enter date in correct format (YYYY-MM-DD).")
                continue

            diff = abs((date2 - date1).days)
            print(f"Difference: {diff} day(s)")
        elif ch == "3":
            d = datetime.datetime.now()
            print("Formatted:", d.strftime("%d-%m-%Y %I:%M %p"))

        elif ch == "4":
            input("Press Enter to start...")
            start = time.time()
            input("Press Enter to stop...")
            end = time.time()
            print("Time:", round(end - start, 2), "seconds")

        elif ch == "5":
            sec = int(input("Enter seconds: "))
            while sec > 0:
                print(sec)
                time.sleep(1)
                sec -= 1
            print("Time up!")

        elif ch == "6":
            break



# MATH MENU
def math_menu():
    while True:
        print("\nMath Menu")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometry")
        print("4. Area of Circle")
        print("5. Back")
        ch = input("Choose: ")

        if ch == "1":
            n = int(input("Enter number: "))
            print("Factorial:", math.factorial(n))

        elif ch == "2":
            p = float(input("Principal: "))
            r = float(input("Rate: "))
            t = float(input("Time (years): "))
            ci = p * (1 + r/100)**t
            print("Compound Interest:", round(ci, 2))

        elif ch == "3":
            a = float(input("Angle (degrees): "))
            rad = math.radians(a)
            print("sin:", round(math.sin(rad), 3))
            print("cos:", round(math.cos(rad), 3))
            print("tan:", round(math.tan(rad), 3))

        elif ch == "4":
            r = float(input("Radius: "))
            print("Area:", round(circle_area(r), 3))

        elif ch == "5":
            break



# RANDOM MENU

def random_menu():
    while True:
        print("\nRandom Menu")
        print("1. Random Number")
        print("2. Random List")
        print("3. Password")
        print("4. OTP")
        print("5. Back")
        ch = input("Choose: ")

        if ch == "1":
            print(random.randint(1, 100))

        elif ch == "2":
            print([random.randint(1, 20) for _ in range(5)])

        elif ch == "3":
            length = int(input("Length: "))
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%"
            pwd = "".join(random.choice(chars) for _ in range(length))
            print("Password:", pwd)

        elif ch == "4":
            print("OTP:", random.randint(100000, 999999))

        elif ch == "5":
            break



# FILE MENU

def file_menu():
    while True:
        print("\nFile Menu")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Back")
        ch = input("Choose: ")

        if ch == "1":
            create_file(input("Filename: "))

        elif ch == "2":
            write_file(input("Filename: "), input("Data: "))

        elif ch == "3":
            read_file(input("Filename: "))

        elif ch == "4":
            append_file(input("Filename: "), input("Data: "))

        elif ch == "5":
            break



# MODULE EXPLORER

def explore():
    name = input("Enter module name: ")
    try:
        mod = __import__(name)
        print(dir(mod))
    except:
        print("Invalid module!")



# MAIN MENU

def main():
    while True:
        print("\n==== MULTI-UTILITY TOOLKIT ====")
        print("1. Datetime and time operations")
        print("2. Mathematical operations")
        print("3. Random Data Geneartions")
        print("4. Generate unique Identifiers (UUID)")
        print("5. File operations (custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        choice = input("Choose: ")

        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            print("UUID:", uuid.uuid4())
        elif choice == "5":
            file_menu()
        elif choice == "6":
            explore()
        elif choice == "7":
            print("Thank you for using Toolkit!")
            break



if __name__ == "__main__":
    main()
