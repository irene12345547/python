age = int(input("Enter studient's age: "))
if age >10:
    if age <20:
        print("Student is eligible for enrollment.")
    else:
        print("Student is NOT eligible.Age is greater than 20.")
else:
    print("Student is NOT eligible.Age is less than 10.")