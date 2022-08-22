import os
import shutil

from_dir = "D:/Coding/Python/Project 102/downloads"
to_dir = "D:/Coding/Python/Project 102/document_files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    name,extension = os.path.splitext(i)
#    print(name)

    if (extension == ""):
        continue
    if (extension in [".txt",".doc",".docx",".pdf",".gif"]):
        path1 = from_dir + "/" + i
        path2 = to_dir + "/" + "document_files"
        path3 = to_dir + "/" + i

        if os.path.exists(path2):
            print("Moving "+ i + ".......")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving "+ i + ".......")
            shutil.move(path1,path3)