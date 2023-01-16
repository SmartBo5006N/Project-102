import os
import shutil

source = r"C:\Users\Lohitaksh\Documents\Python\Project 102"
destination = r"C:\Users\Lohitaksh\Documents\Python\Project 102\documents"

list_Of_documents = os.listdir(source)
print(list_Of_documents)

for x in list_Of_documents:
    name,extension = os.path.splitext(x)
    if extension == "":
        continue
    if extension in ['.pdf', '.txt', '.docx', '.ppt']:
        move_from = source+"/"+x
        check = destination
        move_to = destination+"/"+x
        if os.path.exists(check):
            print("Moving", x)
            shutil.move(move_from, move_to)
        else:
            print("CReating Folder")
            os.mkdir(check)
            print("Moving", x)
            shutil.move(move_from, move_to)    
