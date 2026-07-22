import torch

from transformer import TransformerBlock


x = torch.randn(
    1,
    5,
    128
)


block = TransformerBlock(128)


output = block(x)


print(output.shape)