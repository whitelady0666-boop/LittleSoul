from dataset import EmotionDataset
from tokenizer import LittleTokenizer


t = LittleTokenizer()


d = EmotionDataset(
    "dataset/emotion.jsonl",
    t
)


print("数据数量:", len(d))


x, y = d[0]


print("input:")
print(x)


print("label:")
print(y)