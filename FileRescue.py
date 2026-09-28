print("Welcome to File Rescue. ")
def file():
    folder = input("Which folder do you want to organize? ")
    if not folder:
        print("Please enter a folder")
    else:
        print("scanning:", folder)
file()