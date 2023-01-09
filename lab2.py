from PIL import Image, ImageDraw
picture = Image.new('L', (960, 540), 255) # reating new picture  
inscr = ImageDraw.Draw(picture) # an ImageDraw object is created from this picture

with open("DS4.txt") as file: #opeen file
    for line in file:  #using a loop, the file is divided into lines
        coordArray = line.split()
        inscr.line((int(coordArray[1]), 540 - int(coordArray[0]), int(coordArray[1]) + 1, 540 - (int(coordArray[0]) + 1)))

picture.show() #screening
del inscr
picture.save("DS4_result.jpeg", "JPEG")