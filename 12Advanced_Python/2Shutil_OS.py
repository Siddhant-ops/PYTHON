# # this file consists of using two main built-in modules
# # Shutil and OS modules
# # Shutil stand for Show utilities
# # OS stands for Operating System

# # they are mainly used for opening and reading files and folders

# print("\n================================================================================================\n")

# # Now we will create a new txt file and set it's mode to write

# # creating a new txt file without using w62
# # ith statement

# # f = open('practice.txt', 'w+')
# # f.write("This is a text string")
# # f.close()

# #  now we will create a txt file using with statement

# with open("practice.txt", "w+") as f:
#     f.write("This is practice string")
#     f.close()

# print("\n================================================================================================\n")

# now we will start with OS modules

import os

# # This will print the current working directory

# print(os.getcwd())

# print("\n================================================================================================\n")

# # This will list all the directories in the cwd and it will print it in list

# print(os.listdir())

# print("\n================================================================================================\n")

# # Or we can pass an arg (path name) in listdir and it will print it in list

# print(os.listdir("D:\Main_Folders\siddhant work\VS CODE"))

# print("\n================================================================================================\n")

# # now we will move files around directories with shutil module

# import shutil

# # this method will move my practice txt file to my another folder

# shutil.move(
#     "D:\Main_Folders\siddhant work\VS CODE\PYTHON\practice.txt", "D:\Main_Folders\siddhant work\VS CODE\python_C\practice.txt"
# )

# print("\n==================================================\n")

# # since we have use of practice.txt we would shift it to it's original path

# shutil.move(
#     "D:\Main_Folders\siddhant work\VS CODE\python_C\practice.txt", "D:\Main_Folders\siddhant work\VS CODE\PYTHON\practice.txt"
# )

# # Now there are 3 ways to delete a file or a folder but all of them are very dangerous

# # 1> os.unlink(path) which deletes a file at the path you provide

# # 2> os.rmdir(path) which deletes afolder {folder must be empty} at the path you provide

# # 3> shutil.rmtree(path) this is the most dangrous as will remove all the files and folders contained in the path.

# # All of these methods can not be reversed! Which means if you make a mistake you won't be able to recover the file.

# # Instead we can use send2trash module for deleting files. It is a safer alternative. It sends the files to trash bin instead of permanent removal.

# import send2trash

# print("\n================================================================================================\n")

# print(os.listdir())

# print("\n================================================================================================\n")

# # now we will use send2trash to delete a file

# send2trash.send2trash("practice.txt")

# print("\n================================================================================================\n")

# print(os.listdir())

# print("\n================================================================================================\n")

# # os module has a way of listing all the dirs given in a particular path

# file_path = os.getcwd()

# or u can have fun in C drive by inserting it in file path

file_path_2 = "D:\\"

for folder, sub_folder, files in os.walk(file_path_2):
    print(f"Currently looking in {folder}")
    print("\n")
    print("The sub folders are: ")
    for sub_fold in sub_folder:
        print(f"\tSubFolders are {sub_fold}")

    print("\n")
    print("The files are : ")
    for f in files:
        print(f"\tThe files are {f}")

    print("\n")
