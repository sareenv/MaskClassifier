
'''
    The objective of the Scrapper class is 
    to download and store the images into 
    the training and testing data from the given src.

    Attributes:
    des: Destionation Path for the download and storing the training and testing datasets.
    src: source of the dataset - let's say if we are importing images from the gdrive - 
    we use the function call to download the data.
'''
class Scrapper:
    
    def __init__(self):
        pass
    # src would be the src of the images and des would be the destination 
    # folder if not mentioned it will be current path
    def downloadImages(self, src, des="./"):
        pass

    def deleteImages(self):
        pass
    # splits the images into the training and testing data.
    # the split ratio will be something fixed.
    def splitImages(self):
        pass 
    # In this function the split ratio will be provided with 
    def splitImages(self, ratio):
        pass

    # this will download the images from the internet based on the 
    def downloadImage(self, keyword):
        pass

if (__name__ == "__main__"):
    scapper = Scrapper()
