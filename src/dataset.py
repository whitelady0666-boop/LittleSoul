import json

import torch

from torch.utils.data import Dataset




class EmotionDataset(Dataset):


    def __init__(

        self,

        path,

        tokenizer,

        max_length=128

    ):


        self.data=[]

        self.tokenizer=tokenizer

        self.max_length=max_length



        self.pad_id = tokenizer.token_to_id(
            "<PAD>"
        )


        self.bos_id = tokenizer.token_to_id(
            "<BOS>"
        )


        self.sep_id = tokenizer.token_to_id(
            "<SEP>"
        )


        self.eos_id = tokenizer.token_to_id(
            "<EOS>"
        )



        with open(

            path,

            "r",

            encoding="utf-8"

        ) as f:


            for line in f:


                self.data.append(

                    json.loads(line)

                )




    def __len__(self):

        return len(self.data)




    def __getitem__(
        self,
        idx
    ):


        item=self.data[idx]


        user=item["user"]

        assistant=item["assistant"]



        tokens=[

            self.bos_id

        ]


        tokens += self.tokenizer.encode(
            user
        )


        tokens.append(
            self.sep_id
        )


        tokens += self.tokenizer.encode(
            assistant
        )


        tokens.append(
            self.eos_id
        )



        # GPT训练方式

        x=tokens[:-1]

        y=tokens[1:]



        # 截断

        x=x[:self.max_length]

        y=y[:self.max_length]



        # padding

        while len(x)<self.max_length:


            x.append(
                self.pad_id
            )


            y.append(
                -100
            )



        return (

            torch.tensor(
                x,
                dtype=torch.long
            ),


            torch.tensor(
                y,
                dtype=torch.long
            )

        )