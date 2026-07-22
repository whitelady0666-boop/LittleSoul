import torch

from torch.utils.data import DataLoader, WeightedRandomSampler

from torch.optim import AdamW

from torch.nn import CrossEntropyLoss

from tqdm import tqdm


from model import LittleSoulModel

from dataset import EmotionDataset

from tokenizer import LittleTokenizer



# ======================
# 参数
# ======================

EMBED_DIM = 64

LAYERS = 2

MAX_LEN = 128


EPOCHS = 100

LR = 0.0003

BATCH_SIZE = 8



DEVICE = (
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)



# ======================
# tokenizer
# ======================

tokenizer = LittleTokenizer()


VOCAB_SIZE = len(
    tokenizer.get_vocab()
)


print(
    "VOCAB SIZE:",
    VOCAB_SIZE
)



# ======================
# dataset
# ======================

dataset = EmotionDataset(

    "dataset/emotion.jsonl",

    tokenizer,

    max_length=MAX_LEN

)



print(
    "数据数量:",
    len(dataset)
)



# ======================
# 加权采样
# ======================

weights = []


for item in dataset.data:


    weight = 1.0


    user = item["user"]



    # 长问题提高训练概率

    if "为什么你总能接住" in user:

        weight = 5.0


    elif len(user) > 15:

        weight = 2.0



    weights.append(
        weight
    )



sampler = WeightedRandomSampler(

    weights,

    num_samples=len(dataset),

    replacement=True

)



loader = DataLoader(

    dataset,

    batch_size=BATCH_SIZE,

    sampler=sampler

)



# ======================
# model
# ======================

model = LittleSoulModel(

    vocab_size=VOCAB_SIZE,

    embed_dim=EMBED_DIM,

    layers=LAYERS,

    max_len=MAX_LEN

)



model.to(
    DEVICE
)



# ======================
# optimizer
# ======================

optimizer = AdamW(

    model.parameters(),

    lr=LR

)



# ======================
# loss
# ======================

loss_fn = CrossEntropyLoss(

    ignore_index=-100

)



# ======================
# train
# ======================

model.train()



for epoch in range(EPOCHS):


    total_loss = 0


    progress = tqdm(
        loader
    )


    for x,y in progress:


        x=x.to(
            DEVICE
        )

        y=y.to(
            DEVICE
        )


        optimizer.zero_grad()



        output = model(
            x
        )



        loss = loss_fn(

            output.reshape(
                -1,
                VOCAB_SIZE
            ),

            y.reshape(
                -1
            )

        )



        loss.backward()



        optimizer.step()



        total_loss += loss.item()



        progress.set_description(

            f"Epoch {epoch+1} Loss {loss.item():.4f}"

        )



    avg_loss = (

        total_loss

        /

        len(loader)

    )


    print(

        "平均Loss:",

        avg_loss

    )




# ======================
# save
# ======================

torch.save(

    model.state_dict(),

    "little_soul_final_v2.pt"

)



print(
    "训练完成"
)