import json


with open(
    "tokenizer/vocab.json",
    "r",
    encoding="utf-8"
) as f:

    vocab = json.load(f)


print(len(vocab))