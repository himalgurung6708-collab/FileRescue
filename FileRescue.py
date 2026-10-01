from pathlib import Path

print("Welcome to File Rescue")

def file():
    folder = input("Which folder do you want to organize? ")

    if not folder:
        print("Please enter a folder")
    else:
        print("Scanning:", folder)

        folder_path = Path(folder)
        categories = {
                                        "image": [".jpg", ".jpeg", ".png"],
                                        "documents": [".txt", ".docx", ".pdf"],
                                        "music": [".mp3"],
                                        "video": [".mp4", ".mkv"]
                        
                        
                                    }
        for item in folder_path.iterdir():
            if item.is_file():
                extension = item.suffix.lower()
                for category, extensions in categories.items():
                    if extension in extensions:
                        print(f"Your file is {category}")
                    
                    print("FILE:", item)
            elif item.is_dir():
                print("FOLDER:", item)

file()