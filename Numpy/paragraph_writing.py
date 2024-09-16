# import numpy as np
import re

# with open("paragraph.txt", "w") as file:

#     a = ""
#     while a!="1":
#         a = input("")
#         file.writelines(a + "\n")

line = ""
with open("paragraph.txt", "r") as file:
    
    l = file.readlines()
    for blue in l:
        line+=blue
        
igst= re.search(r'IGST\s*\:\s*([\d]{4})', line, re.IGNORECASE)
print(igst) 