import torch

from positional import PositionalEncoding


x = torch.zeros(
    1,
    5,
    128
)


pe = PositionalEncoding(
    128
)


output = pe(x)


print(output.shape)