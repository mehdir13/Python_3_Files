#### Reading a file

- Write a Python script that reads a file and prints its contents to the console. Create a text file with several lines of text for testing purposes.
- Additional: Modify the script to read the file line by line and print each one with its line number.

with open("hello.txt", "w") as my_file:
    my_file.write("Hello world \n")
    my_file.write("I hope you're doing well today \n")
    my_file.write("This is a text file \n")
    my_file.write("Have a nice time \n")

with open("hello.txt") as my_file:
    print(my_file.read())

with open("hello.txt") as my_file:
    for line in my_file:
        print(line)

# Output: 
# Hello world 
# I hope you're doing well today
# This is a text file
# Have a nice time


#### Copying a file
- Write a program that copies the contents of one file to another file.
- Additional: Modify the script to only copy lines that contain a specific word.