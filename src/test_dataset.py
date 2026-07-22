from dataset import EmotionDataset
from tokenizer import LittleTokenizer


tokenizer = LittleTokenizer()


dataset = EmotionDataset(
    "dataset/emotion.jsonl",
    tokenizer
)


print(
    len(dataset)
)


x,y = dataset[0]


print(x)

print(y)