# assignment4


Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
fh = open("sample.txt", 'wt')
fh.write("Hello World\n")
fh.write("Let us learn Python")
fh.close()

3.   Prints its content line by line.
4.   Handles errors gracefully if the file does not exist.

try:
    fh = open("sample.txt", 'rt')
    line1 = fh.readline()
    line2 = fh.readline()
    print("Reading file content\n")
    print(f"Line 1: {line1}")
    print(f"Line 2: {line2}")
    fh.close()

except FileNotFoundError:
    print("Error: File \"sample1.txt\" does not exist")


    ```````````````````````````````````````````````````````````
  
 Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
file_handler = open("output.txt", "wt")
text1 = input("Please enter a text that you want to write in the file:")
file_handler.write(text1)
file_handler.close()


3.   Appends additional data to the same file.
text2 = input("Please enter a text that you want to append to the file:")
file_handler = open("output.txt", "at")
file_handler.write(text2)
file_handler.close()

5.   Reads and displays the final content of the file.

print("Final output of the file")
fh = open("output.txt","rt")
lines = fh.readlines()
for line in lines:
    print(line)



    
