#!/usr/bin/python3
output = ""
for element in "abcdefghijklmnopqrstuvwxyz":
    if element.isupper():
        output += f"Uppercase letter found: {element}\n"
    else:
        output += f"Uppercase letter not found: {element}\n"
print(output, end="")

