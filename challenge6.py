# http://www.pythonchallenge.com/pc/def/channel.html  
import zipfile

# "readme.txt" tells us to start here 
firstFile = "channel/90052.txt"

# Turns out a zipfile can have comments
# They can be accessed using the ZipFile python library

# Create a ZipFile object: 
zip = zipfile.ZipFile("/Users/nate/Desktop/python/channel.zip")

comments = [] 

def nextFile(f):
    contents = open(f).read()
    nothing = '' 
    for c in contents:
        if c.isdigit():
            nothing += c
    comment = zip.getinfo(nothing + ".txt").comment.decode()
    comments.append(comment)
    print(contents + "      from:" + f)
    return ("channel/" + nothing + ".txt")

def scanNFiles(n,f):
    if n==0:
        return "Done"
    else:
        newf = nextFile(f)
        scanNFiles(n-1,newf) 


# scan for awhile then run
# >>> print("".join(challenge6.comments))
        


