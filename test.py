import numpy
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
# print(l)


# Basic operations

a = torch.rand(2, 2)
b = torch.rand(2, 2)
# print(a)
# print(b)

add = a+b
# # print(add)

b.add_(a)
# print(b)

# Slicing

# a = torch.rand(2, 2)
# print(a)
# print(a[1, :])

# Numpy to torch tensor

a = torch.ones(2, 3)
print(type(a))
b = a.numpy()
print(type(b))
