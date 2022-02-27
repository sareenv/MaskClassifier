import torch 
import numpy as np 

# switches from the cpu to the gpu for the model training.
device = None
if torch.cuda.is_available():
    device = torch.device("cuda")
    
else:
    device = torch.device("cpu")

x = torch.ones(5, device=device)
y = torch.zeros(5)
result = x + y
# converts back to the cpu - this is required.
if (device == torch.device("cuda") ):
    result = torch.to("cpu") 
    
print("tensor result is {}".format(result))
