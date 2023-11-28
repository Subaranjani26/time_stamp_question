#Question-1

import datetime

def createtextfile_timestamp():
    emptyfile = datetime.datetime.now().strftime("%y-%m-%d_%H-%M-%S")
    newfile = f"textfile{emptyfile}.txt"
    with open(newfile,'w') as file:
        file.write("create a text file with current timestamp")
    print(f"created textfile:{newfile}")
createtextfile_timestamp()


#Question-2

def readtextfile(newfile):
    try:
        with open (newfile,'r') as file:
            storagefile = newfile.read()
            print(f"read textfile:{newfile}")
    except:
        print(f"error:{newfile}")
readtextfile('textfile23-11-27_20-19-53.txt')
