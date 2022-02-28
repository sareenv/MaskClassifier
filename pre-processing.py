import cv2 
import matplotlib.pyplot as plt
import os
import sys
from PIL import Image
import dropbox


'''

    Reference: 
        # ref: https://stackoverflow.com/questions/21517879/python-pil-resize-all-images-in-a-folder

'''

class ProcessingUtility:

    def __init__(self, base_path, output_path, dimension):
        load_dotenv() 
        # custom path to my desktop location needs to be init with constructor if runs on someone else's computer
        self.base_path = base_path
        self.output_path = output_path     
        dirs = os.listdir(base_path)
        self.dirs = dirs
        self.base_path = base_path
        self.dimensions = dimension


    def resizer(self, out_format = "JPEG", mode = Image.ANTIALIAS):
        print("base path is {}".format(self.base_path))
        cnter = 0
        for item in self.dirs:
            location = self.base_path + item
            if os.path.isfile(location):
                # here the files are found from the src. 
                image = Image.open(location)
                # plt.imshow(image)
                # plt.show() - tested images are being loaded properly.
                # break
                
                # produces the resized image of desired dimensions. 
                resized_image = image.resize(self.dimensions, mode)
                out_format = "JPEG"
                output_location = self.output_path + str(cnter) + "_resized.jpeg"
                resized_image.save(output_location, out_format, quality=90)
        
        cnter += 1
        print("done processing images !")



    def imageAugmentationProcessing(self):
        pass

    def imageSegmentation(self):
        pass

    def imageRGBTransformation(self):
        pass

    def deleteImages(self):
        pass

if (__name__ == "__main__"):
    inp_location = input("Enter the input file location:  ")
    output_location = input("Enter the output file location: ")
    dimension_x = int(input("Enter the dimensions x: "))
    dimension_y = int(input("Enter the dimensions y: "))
    dimension = (dimension_x, dimension_y)
    utility = ProcessingUtility(inp_location, output_location, dimension)
    utility.resizer()


