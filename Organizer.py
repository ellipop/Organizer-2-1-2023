import os
import shutil
destination = "/Users/oscarrodriguez/Downloads"
source = "/Users/oscarrodriguez/Documents/test/imageFile"
listofFiles = os.listdir(source)



for fileName in listofFiles:
    name,extention = os.path.splitext(fileName)
    if extention == "":
        continue
    if extention in [ ".jpg", ".mov", ".png"]:
        path1 = source + "/" + fileName
        path2 = destination + "/" + "imageFile"
        path3 = destination + "/" + "imageFile" + "/" + fileName
        if os.path.exists(path2):
            print("moving " + fileName + "...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("moving " + fileName + "...")
            shutil.move(path1,path3)

