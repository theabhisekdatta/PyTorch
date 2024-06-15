import torch

# Creating empty tensors
x = torch.empty(3, 2)
# print(x)

# Create random tensors
r = torch.rand(2, 3)
# print(r)

# Create zero or ones tensors
z = torch.zeros(2, 3)
# print(z)
o = torch.ones(2, 3)
# print(o)

# Change the data types
o = torch.ones(2, 3, dtype=torch.int)
# print(o.dtype)

# Create Tensor from List

l = torch.tensor([2.5, 6.4])
print(l)
