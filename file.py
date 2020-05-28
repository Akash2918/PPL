import os

print("Enter the path of the file :")

path = input()
#print("The enterd path is : " + path)

try :
    os.path.exists(path)
    if os.path.isdir(path):
        print("Getting the contents of the folder")
        #content = os.listdir(path)
        #print(content)
        print()
        print()
        print("File Name ", " " , "Size")
        for filename in os.listdir(path):
            size = os.path.getsize(os.path.join(path, filename))
            print(filename, " ", size)

        totalsize = 0
        for filename in os.listdir(path):
            totalsize = totalsize + os.path.getsize(os.path.join(path, filename))

        
        print()
        print()
        print("The total size of the folder is (In bytes) {}:".format(totalsize))
        #print(totalsize)

    elif os.path.isfile(path) :
        print("Getting file size (in bytes) :")
        print(os.path.getsize(path))

except FileNotFoundError :
    print("The required file or folder does not exist at given location")
    print("Please try again")

except :
    print("Please try again")



