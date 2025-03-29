import os
import shutil

folder_path = "C:/Users/ANC/Downloads"

file_categories = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"],
    "Scripts": [".py", ".js", ".html"],
}

def organized_files():
    if not os.path.exists(folder_path):
        print("Folder does not exist!")
        return

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(file)

        for categories , extensions in file_categories.items():
            if ext.lower() in extensions:
                categories_path = os.path.join(folder_path, categories)
                if not os.path.exists(categories_path):
                    os.makedirs(categories_path)  # Create folder if not exists
                shutil.move(file_path, os.path.join(categories_path, file))
                print(f"Moved {file} to {categories}/")

            print("File organization complete!")

            # Run the function
            organized_files()
