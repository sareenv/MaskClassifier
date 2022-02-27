import torch
import numpy as np
import matplotlib.pyplot as plt

class Model:
    
    '''
        Parametrised constructor which accepts few hyper-parameters required for the model training 
        and includes lr = learning rate, optimiser for optimisation, Architecture - this will be the object of 
        CNN Architecture.
    '''
    def __init__(self, lr, optimiser, Architecture = None) -> None:
        pass

    '''
        Loads the data from the respective folders, if not mentioned default is the current path of the project 
        for loading the required data.
    '''

    def load_data(self, folder_path = "./"):
        pass

    '''
        The method applies the learning of the network from the current training sample.
    '''
    def fit(self):
        pass

    '''
        The method predicts against the given input test sample.
    '''
    def test(self, input_imagePath = None):
        pass

if(__name__ == "__main__"):
    pass