import json
import os


class LittleTokenizer:


    def __init__(self):

        # 项目根目录
        base_dir = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )


        self.tokenizer_dir = os.path.join(
            base_dir,
            "tokenizer"
        )


        self.vocab_path = os.path.join(
            self.tokenizer_dir,
            "vocab_char.json"
        )


        self.data_path = os.path.join(
            base_dir,
            "dataset",
            "emotion.jsonl"
        )


        self.special_tokens = [

            "<PAD>",
            "<UNK>",
            "<BOS>",
            "<EOS>",
            "<SEP>"

        ]


        if os.path.exists(
            self.vocab_path
        ):

            self.load_vocab()

        else:

            self.build_vocab()



    # ======================
    # 创建词表
    # ======================

    def build_vocab(self):


        chars=set()



        with open(
            self.data_path,
            "r",
            encoding="utf-8"
        ) as f:


            for line in f:

                item=json.loads(line)


                chars.update(
                    list(item["user"])
                )


                chars.update(
                    list(item["assistant"])
                )



        self.vocab={}


        index=0



        for token in self.special_tokens:


            self.vocab[token]=index

            index+=1



        for ch in sorted(chars):


            if ch not in self.vocab:

                self.vocab[ch]=index

                index+=1



        self.id_to_token={

            v:k

            for k,v in self.vocab.items()

        }



        os.makedirs(
            self.tokenizer_dir,
            exist_ok=True
        )



        with open(
            self.vocab_path,
            "w",
            encoding="utf-8"
        ) as f:


            json.dump(
                self.vocab,
                f,
                ensure_ascii=False,
                indent=2
            )



        print(
            "创建字符词表:",
            len(self.vocab)
        )




    # ======================
    # 加载词表
    # ======================

    def load_vocab(self):


        with open(
            self.vocab_path,
            "r",
            encoding="utf-8"
        ) as f:


            self.vocab=json.load(f)



        self.id_to_token={

            int(v):k

            for k,v in self.vocab.items()

        }




    # ======================
    # encode
    # ======================

    def encode(
        self,
        text
    ):


        ids=[]


        for ch in text:


            ids.append(

                self.vocab.get(

                    ch,

                    self.vocab["<UNK>"]

                )

            )


        return ids




    # ======================
    # decode
    # ======================

    def decode(
        self,
        ids
    ):


        text=""


        for idx in ids:


            token=self.id_to_token.get(

                int(idx),

                ""

            )


            if token in self.special_tokens:

                continue



            text+=token



        return text




    # ======================
    # 工具
    # ======================

    def token_to_id(
        self,
        token
    ):

        return self.vocab[token]



    def get_vocab(self):

        return self.vocab