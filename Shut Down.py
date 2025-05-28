def shutdown(command):
    if command.lower() == "yes":
        print("Abort shut down ...")
    elif command.lower() == "no":
        print("Abort shut down!")
    else:
        print("Sorry.")
user_input = input("Do you want to shut down the system? (Yes/No): ")
shutdown(user_input)