from pathlib import Path

print("Welcome to File Rescue")

def file():
    folder = input("Which folder do you want to organize? ")

    if not folder:
        print("Please enter a folder")
    else:
        print("Scanning:", folder)

        folder_path = Path(folder)

        for item in folder_path.iterdir():

            if item.is_file():
                print("FILE:", item)

            elif item.is_dir():
                print("FOLDER:", item)

file()