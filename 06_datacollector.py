

# Welcome Message
print("====================================")
print(" Welcome to Personal Data Collector ")
print("====================================")
print("This program will collect your personal details.")
print("Please follow the instructions and enter right details.")
print()

# --- Collect Information ---
name = input("Enter your full name: ")
age= input("Enter your age: ")
height = input("Enter your height : ")
weight = input("Enter your weight: ")
email = input("Enter your email address: ")
birthdate = input("Enter your birthdate: ")

# --- (Type Casting) ---
age = int(age) 
height_cm = float(height)  
weight_kg = int(weight)

# --- Result ---
print("====== yourself ==========")
print (name)
print( age)
print(height_cm)
print( weight_kg)
print(email)


# --- ID & TYPE Info ---

print("Data type of age        :", type(age), "Memory ID:", id(age))
print("Data type of height_cm  :", type(height_cm), " Memory ID:", id(height_cm))
print("Data type of name       :", type(name), " Memory ID:", id(name))
print("data type of birthdate  :", type(birthdate), "memory  ID:", id(birthdate))


print("===================================")
print("        AGE CLASSIFICATION         ")
print("===================================")

print("Based on your age:")

if age < 0:
    print("Invalid age entered.")
elif age <= 12:
    print(" You are a Child.")
elif 13 <= age <= 19:
    print(" You are a Teenager.")
elif 20 <= age <= 35:
    print(" You are a Young Adult.")
elif age >= 60:
    print(" You are a Senior Citizen.")
else:
    print(" Age classification not found.")


print("====================================")
print("Thank you", name,"")
print("have a great day!")
print("====================================")