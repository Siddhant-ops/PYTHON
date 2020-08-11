print("================================================================================================")

# Good work on unzipping the file!
# You should now see 5 folders, each with a lot of random .txt files.
# Within one of these text files is a telephone number formated ###-###-####
# Use the Python os module and regular expressions to iterate through each file, open it, and search for a telephone number.
# Good luck!

# The path of the folder to search at :

import os, shutil, re

folder_path = "C:\\siddhant work\\VS CODE\\python_C\\Complete-Python-3-Bootcamp-master\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise\\unzip_me\\extracted_content"


def search(file, pattern=r"\d{3}-\d{3}-\d{4}"):
    f = open(file, "r")
    text = f.read()

    if re.search(pattern, text):
        print(f"{file}\n")
        return re.search(pattern, text)
    else:
        return ""


search_found = []

for folder, sub_folder, files in os.walk(folder_path):

    for f in files:
        fold = folder + "\\" + f

        search_found.append(search(fold))

print(search_found)


for r in search_found:
    if r != "":
        print(r.group())

