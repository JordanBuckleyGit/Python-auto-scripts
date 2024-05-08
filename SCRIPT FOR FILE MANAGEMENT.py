import os
import shutil

source_dir = "/Users/jorda/Downloads"
target_dir = "/Users/jorda/School-Work-Folder"

EXTS = ("doc", "docx")

# Display the menu
def menu():
    while(True):
        print("\n--Welcome To The Automatic Script Menu--")
        print("_" * 35)
        print("1. Move Doc Files from Downloads to School/Work folder")
        print("2. Creating a calender script")
        print("")
        print("0. Exit")
        print("_" * 35)
        option = int(input("Choose an option (0-5): "))
        print("\n")

        if option == 1:
            move_files(source_dir, target_dir)
        elif option == 2:
            print('function yet to be added')
        elif option == 0:
            break
        else:
            print("Sorry, this option does not exist!")
if __name__ == "__main__":
    menu()


def move_files(source_dir, target_dir):
    files = os.listdir(source_dir)
    for file in files:
        if file.lower().endswith(EXTS):
            source_path = os.path.join(source_dir, file)
            target_path = os.path.join(target_dir, file)
            shutil.move(source_path, target_path)
            print(f"Moved {file} to {target_dir}")
# Call the function to move files

