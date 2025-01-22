#### Copying a file
# - Write a program that copies the contents of one file to another file.

def copy_file_contents(source_file_path, destination_file_path):
    try:
        with open(source_file_path, 'r') as source_file:
            contents = source_file.read()
        
        with open(destination_file_path, 'w') as destination_file:
            destination_file.write(contents)
            
        print(f"Contents copied from '{source_file_path}' to '{destination_file_path}' successfully.")
    except FileNotFoundError:
        print(f"The file '{source_file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file_path = 'newsample.txt'
destination_file_path = 'destination.txt'  # file will be created if it doesn't exist

with open("newsample.txt", "r") as f:
    print(f.read())
print("-------------<><><><><><><><><><<><><><>------------------------------------")

copy_file_contents(source_file_path, destination_file_path)

print("-------------<><><><><><><><><><<><><><>------------------------------------")    

with open("destination.txt", "r") as f:
    print("THIS IS THE CONTENT OF THE COPIED FILE:")
    print(" ")
    print(f.read())
print("-------------<><><><><><><><><><<><><><>------------------------------------")



print("-----------------------------------------------------------------------------------------------------------------------")

# - Additional: Modify the script to only copy lines that contain a specific word.

def copy_lines_with_word(source_file_path, destination_file_path, specific_word):
    try:
        with open(source_file_path, 'r') as source_file:
            with open(destination_file_path, 'w') as destination_file:
                for line in source_file:  # Read the source file line by line # "LINE" is a string variable
                    if specific_word in line.lower():  # Check if the specific word is in the line # ".lower()" converts all the content in both specific-word and line into lowercase: case-insensitive search.
                        destination_file.write(line)  # Write the line to the destination file

        print(f"Lines containing '{specific_word}' have been copied from '{source_file_path}' to '{destination_file_path}'.")
    except FileNotFoundError:
        print(f"The file '{source_file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


source_file_path = 'newsample.txt'
destination_file_path = 'destination.txt'
specific_word = 'test'

copy_lines_with_word(source_file_path, destination_file_path, specific_word)

with open("destination.txt", "r") as f:
    print("HERE IS THE COPIED LINES INCLUDING IT:")
    print(" ")
    print(f.read())
print("-------------<><><><><><><><><><<><><><>------------------------------------")

