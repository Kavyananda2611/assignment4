"""
 Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

"""

file_handler = open("output.txt", "wt")
text1 = input("Please enter a text that you want to write in the file:")
file_handler.write(text1)
file_handler.close()
text2 = input("Please enter a text that you want to append to the file:")
file_handler = open("output.txt", "at")
file_handler.write(text2)
file_handler.close()

print("Final output of the file")
fh = open("output.txt","rt")
lines = fh.readlines()
for line in lines:
    print(line)
