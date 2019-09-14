from PIL import Image
import os,sys
def createNewDirectory(directoryPath):
    if not os.path.exists(directoryPath):
        os.makedirs(directoryPath)
    
def imageParser(pathName):
    directory = os.listdir(pathName)
    print(directory) 
    for item in directory:
        #pathToFile = os.path.join(pathName+item)
        if os.path.isfile(pathName+item):
            img = Image.open(pathName+item)
            file, extension = os.path.splitext(pathName+item)
            print(file+"\n")
            print(extension+"\n")
            imResize = img.resize((1440,1080), Image.ANTIALIAS)
            imResize.save(file + '_resized.jpg', 'JPEG', quality=90)
        else:
            print(pathName+item+" not found")
#https://stackoverflow.com/questions/21517879/python-pil-resize-all-images-in-a-folder