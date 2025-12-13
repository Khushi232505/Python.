import os

def print_directory_contents(path='/ '):
    try:
        entries = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for item in entries:
            print(item)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except NotADirectoryError:
        print(f"Error: The path '{path}' is not a directory.")
    except PermissionError:
        print(f"Error: Permission denied for accessing '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # To list current directory:
    print_directory_contents()
    # To specify another directory:
    # print_directory_contents('/path/to/your/directory')
