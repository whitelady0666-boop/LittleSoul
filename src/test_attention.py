import torch

from attention import SelfAttention


x = torch.randn(
    1,
    5,
    128
)


attention = SelfAttention(128)


output = attention(x)


print(output.shape)