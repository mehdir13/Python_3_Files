#### Reading a file

# - Write a Python script that reads a file and prints its contents to the console. Create a text file with several lines of text for testing purposes.

def read_file_function(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'newsample.txt'
read_file_function(file_path)

print("-----------------------------------------------------------------------------------------------------------------------")
# - Additional: Modify the script to read the file line by line and print each one with its line number.

def read_file_line_by_line_function(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):  # Enumerate starts from 1. Line number + line content
                print(f"{line_number}: {line.strip()}")  # Print line number and content
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'newsample.txt'
read_file_line_by_line_function(file_path)
