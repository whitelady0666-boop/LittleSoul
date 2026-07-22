import torch

from model import LittleSoulModel


model = LittleSoulModel(
    vocab_size=400,
    embed_dim=128,
    layers=4
)


x = torch.randint(
    0,
    400,
    (
        1,
        5
    )
)


output = model(x)


print(output.shape)