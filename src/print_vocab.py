from tokenizers import ByteLevelBPETokenizer


tokenizer = ByteLevelBPETokenizer(
    "tokenizer/vocab.json",
    "tokenizer/merges.txt"
)


print(
    "词表大小:",
    tokenizer.get_vocab_size()
)


for token, idx in tokenizer.get_vocab().items():

    if token.startswith("<"):

        print(
            token,
            idx
        )