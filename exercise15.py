# Reading Files
from sys import argv   # it uses argv to get a filename
script, filename = argv #it uses argv to get a filename
txt = open(filename)   

print(f"Here;s your file {filename}:")  #prints a little message.
print(txt.read())  # We call a function on txt named read.

print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)

print(txt_again.read()) 


# from sys import argv mean, sys is a package, and this phrase just says to get the argv feature from that package.