"""
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

"""
fh = open("sample.txt", 'wt')
fh.write("Hello World\n")
fh.write("Let us learn Python")
fh.close()

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