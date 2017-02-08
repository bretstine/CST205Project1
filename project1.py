from PIL import Image
import time

def medianOdd(pictures):
    # Store list length in variable listLength
    listLength = len(pictures)
    # Sort the list
    sortedValues = sorted(pictures)
    # Location of middle value. Subtract one because of zero index
    middleIndex = ( (listLength + 1) // 2) - 1
    # Return the object located at that index
    return sortedValues[middleIndex]

# function used to read pictures into array
def readPictures(numPics, directory , pictures):
    for i in range(numPics):
        filename = directory + "/" + str(i + 1) + ".png"
        pictures.append( Image.open(filename) )

# create an empty list
images = []

start_timer = time.time()

# call the function, after function call
# the image objects should be loaded into pictures list
readPictures(9,"Project1Images",images)

pictureWidth, pictureHeight = images[0].size
redPixelList = []
greenPixelList = []
bluePixelList = []

finalImage = Image.new('RGB', (pictureWidth, pictureHeight) )  

for x in range(0, pictureWidth):
    for y in range(0, pictureHeight):
        for myImage in images:
            r, g, b = myImage.getpixel((x,y))
                
            redPixelList.append(r)
            greenPixelList.append(g)
            bluePixelList.append(b)
        
        finalImage.putpixel( (x,y) , (medianOdd(redPixelList), medianOdd(greenPixelList), medianOdd(bluePixelList) ) )
        
        redPixelList = []
        greenPixelList = []
        bluePixelList = []

finalImage.save("FinalImage.png")

print("--- %s seconds ---" % (time.time() - start_timer))