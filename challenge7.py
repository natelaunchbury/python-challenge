# http://www.pythonchallenge.com/pc/def/oxygen.html 

# image-processing library 
from PIL import Image

img = Image.open('oxygen.png')

#print(img.width)

# testing function 
def getPixels(w,h):
  for i in range(0,h):
     for j in range(0,w):
       pixel = img.getpixel((i,j))
       print("(" + str(i) + ',' + str(j) + "): " + str(pixel))

# grey is when the rgb values are all equal 
def isGrey(p):
    return (p[0]==p[1] and p[0]==p[2])

# all the grey pixels
def getGreys(img):
    greyPixels = []
    for w in range(0,img.width):
        for h in range(0,img.height):
            pixel = img.getpixel((w,h))
            if isGrey(pixel):
                greyPixels.append(pixel)
    return greyPixels

# list comprehension to just get the ones on the middle line in the image  
# the list is filtered for grey pixels only and decouples the groups of 7 identical pixels
greys = [img.getpixel((x,img.height/2)) 
        for x in range(0,img.width) if isGrey(img.getpixel((x,img.height/2)))][::7]

# decode the numbers into ASCII 
message = "".join(map(chr,[p[0] for p in greys]))

print(message)



