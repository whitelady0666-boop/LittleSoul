import torch

from model import LittleSoulModel
from tokenizer import LittleTokenizer
from memory import LittleMemory



# ======================
# 参数
# ======================


EMBED_DIM=64

LAYERS=2


DEVICE="cpu"


MODEL_PATH="little_soul_final.pt"



# ======================
# tokenizer
# ======================


tokenizer=LittleTokenizer()


VOCAB_SIZE=len(
    tokenizer.get_vocab()
)



bos_id=tokenizer.token_to_id(
    "<BOS>"
)


sep_id=tokenizer.token_to_id(
    "<SEP>"
)


eos_id=tokenizer.token_to_id(
    "<EOS>"
)



print(
    "VOCAB:",
    VOCAB_SIZE
)


print(
    "BOS:",
    bos_id,
    "SEP:",
    sep_id,
    "EOS:",
    eos_id
)



# ======================
# memory
# ======================


memory=LittleMemory()



# ======================
# model
# ======================


model=LittleSoulModel(

    vocab_size=VOCAB_SIZE,

    embed_dim=EMBED_DIM,

    layers=LAYERS

)



model.load_state_dict(

    torch.load(

        MODEL_PATH,

        map_location=DEVICE

    )

)



model.eval()



# ======================
# normalize
# ======================


def normalize(text):


    replace={

        "?":"？",

        "!":"！",

        ",":"，",

        ".":"。"

    }


    for a,b in replace.items():

        text=text.replace(
            a,
            b
        )


    return text.strip()



# ======================
# generate
# ======================


def generate(
    text,
    max_tokens=80
):


    tokens=[]


    tokens.append(
        bos_id
    )


    tokens.extend(
        tokenizer.encode(
            text
        )
    )


    tokens.append(
        sep_id
    )



    input_ids=torch.tensor(

        [tokens],

        dtype=torch.long

    )



    generated=[]



    for _ in range(max_tokens):


        with torch.no_grad():


            output=model(
                input_ids
            )



        logits=output[:,-1,:]



        # 禁止特殊token


        logits[0][bos_id]=-float("inf")


        logits[0][sep_id]=-float("inf")



        probs=torch.softmax(
            logits,
            dim=-1
        )



        next_token=torch.argmax(
            probs,
            dim=-1
        ).item()



        if next_token==eos_id:

            break



        generated.append(
            next_token
        )



        input_ids=torch.cat(

            [

                input_ids,

                torch.tensor(
                    [[next_token]]
                )

            ],

            dim=1

        )



    return tokenizer.decode(
        generated
    )



# ======================
# chat
# ======================


while True:


    user=input(
        "你："
    )



    if user=="exit":

        break



    user=normalize(
        user
    )



    # ======================
    # memory优先
    # ======================


    answer=memory.search(
        user
    )



    if answer:


        print(
            "LittleSoul：",
            answer
        )


        continue



    # ======================
    # 模型生成
    # ======================


    response=generate(
        user
    )



    print(
        "LittleSoul：",
        response
    )