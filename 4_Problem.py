# write a python program to print the contents of a directory using the os module
# Search online for the function which does that



import os

def list_directory_contents(path="."):
    try:
        contents = os.listdir(path)
        print(f"Contents of directory '{os.path.abspath(path)}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print("The specified path was not found.")
    except PermissionError:
        print("Permission denied to access this path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
directory_path = '.'  # You can change this to any path you want
list_directory_contents(directory_path)
