import torch
import torch.nn as nn
import torch.nn.functional as F


class SelfAttention(nn.Module):


    def __init__(self, embed_dim):

        super().__init__()


        self.query = nn.Linear(
            embed_dim,
            embed_dim
        )


        self.key = nn.Linear(
            embed_dim,
            embed_dim
        )


        self.value = nn.Linear(
            embed_dim,
            embed_dim
        )



    def forward(self,x):


        B,T,C=x.shape


        Q=self.query(x)

        K=self.key(x)

        V=self.value(x)



        scores=torch.matmul(
            Q,
            K.transpose(-2,-1)
        )


        scores=scores/(C**0.5)



        # causal mask

        mask=torch.triu(
            torch.ones(
                T,
                T,
                device=x.device
            ),
            diagonal=1
        )


        scores=scores.masked_fill(
            mask==1,
            float("-inf")
        )



        weights=F.softmax(
            scores,
            dim=-1
        )


        output=torch.matmul(
            weights,
            V
        )


        return output