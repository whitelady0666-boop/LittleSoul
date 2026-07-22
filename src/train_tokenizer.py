from tokenizers import ByteLevelBPETokenizer
import os


tokenizer = ByteLevelBPETokenizer()


files = [
    "dataset/emotion.jsonl"
]


tokenizer.train(
    files=files,
    vocab_size=2000,
    min_frequency=1,
    special_tokens=[
        "<PAD>",
        "<UNK>",
        "<BOS>",
        "<EOS>",
        "<SEP>"
    ]
)


os.makedirs(
    "tokenizer",
    exist_ok=True
)


tokenizer.save_model(
    "tokenizer"
)


print("Tokenizer训练完成！")