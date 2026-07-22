import torch
import torch.nn as nn

from transformer import TransformerBlock



class LittleSoulModel(nn.Module):


    def __init__(
        self,
        vocab_size,
        embed_dim=64,
        layers=2,
        max_len=128
    ):

        super().__init__()



        self.token_embedding=nn.Embedding(
            vocab_size,
            embed_dim
        )


        self.position_embedding=nn.Embedding(
            max_len,
            embed_dim
        )



        self.blocks=nn.ModuleList(

            [

                TransformerBlock(
                    embed_dim
                )

                for _ in range(layers)

            ]

        )



        self.norm=nn.LayerNorm(
            embed_dim
        )


        self.head=nn.Linear(
            embed_dim,
            vocab_size
        )



        self.max_len=max_len




    def forward(
        self,
        x
    ):


        B,T=x.shape


        pos=torch.arange(

            T,

            device=x.device

        )


        pos=pos.unsqueeze(0).expand(
            B,
            T
        )


        x=(

            self.token_embedding(x)

            +

            self.position_embedding(pos)

        )



        for block in self.blocks:

            x=block(x)



        x=self.norm(x)


        return self.head(x)