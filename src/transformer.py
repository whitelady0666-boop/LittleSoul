import torch
import torch.nn as nn



class MultiHeadAttention(nn.Module):


    def __init__(
        self,
        embed_dim,
        heads=4
    ):

        super().__init__()


        self.heads=heads

        self.head_dim=embed_dim//heads


        self.qkv=nn.Linear(
            embed_dim,
            embed_dim*3
        )


        self.proj=nn.Linear(
            embed_dim,
            embed_dim
        )




    def forward(self,x):


        B,T,C=x.shape


        qkv=self.qkv(x)


        q,k,v=qkv.chunk(
            3,
            dim=-1
        )


        q=q.view(
            B,
            T,
            self.heads,
            self.head_dim
        ).transpose(1,2)


        k=k.view(
            B,
            T,
            self.heads,
            self.head_dim
        ).transpose(1,2)


        v=v.view(
            B,
            T,
            self.heads,
            self.head_dim
        ).transpose(1,2)



        score=(

            q @ k.transpose(-2,-1)

        ) / (

            self.head_dim **0.5

        )



        mask=torch.triu(

            torch.ones(
                T,
                T,
                device=x.device
            ),

            diagonal=1

        )



        score=score.masked_fill(

            mask==1,

            float("-inf")

        )



        attn=torch.softmax(
            score,
            dim=-1
        )


        out=attn@v



        out=out.transpose(
            1,
            2
        ).contiguous()


        out=out.view(
            B,
            T,
            C
        )


        return self.proj(out)




class TransformerBlock(nn.Module):


    def __init__(
        self,
        embed_dim
    ):

        super().__init__()



        self.attn=MultiHeadAttention(
            embed_dim
        )


        self.norm1=nn.LayerNorm(
            embed_dim
        )


        self.norm2=nn.LayerNorm(
            embed_dim
        )



        self.ffn=nn.Sequential(

            nn.Linear(
                embed_dim,
                embed_dim*4
            ),

            nn.GELU(),

            nn.Linear(
                embed_dim*4,
                embed_dim
            )

        )



    def forward(
        self,
        x
    ):


        x=x+self.attn(
            self.norm1(x)
        )


        x=x+self.ffn(
            self.norm2(x)
        )


        return x