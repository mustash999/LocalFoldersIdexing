#Genius Panda  - Folders and subfolders Indexing - wrting in a txt file 
#Version 1 :::::::  Dec 2020



#Importing library 
import os
import os.path
import glob

# Function Thats reads subfolders and add it to the main list
 
def lsdir(path):
    dirlst= os.listdir(path)
    folderpaths=[]
    for item in dirlst:
        itmpath = path + "/" + item
        if os.path.isdir(itmpath):
            folderpaths.append(itmpath)
            print(itmpath)
    return folderpaths

#Identifying the main Folder // drive 

path=input("Enter the path to folder:  Example:: C:\\Windows\\")
if path == None:
    path= "C:\\"
mainfolder= path.replace("\\", "/")


txtfile= input("Enter the file name [txtfile.txt] ")
if txtfile == None:
    txtfile="txtfile.txt"




#Creating the seed list 
remainingpath= lsdir(mainfolder)


#Looping thorughtout the list  writing results to a text file
while len(remainingpath) > 0:
    with open( txtfile, "a") as f:
        for folder in remainingpath:
            try:
                print((str(folder.encode("utf-8")))+",", file=f)
                newitems= lsdir(folder)
                remainingpath.extend(newitems)
                remainingpath.remove(folder)
            except PermissionError:
                remainingpath.remove(folder)
            
            


