import numpy as np

with open("paragraph.txt", "a") as file:

    a = ""
    while a!="1":
        a = input("")
        file.writelines(a + "\n")


with open("paragraph.txt", "r") as file:
    line = file.readlines()
    for lines in line:
        print(lines, end = " ") 