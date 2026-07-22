from tokenizer import LittleTokenizer

tokenizer = LittleTokenizer()

text = "今天工作很累。"

ids = tokenizer.encode(text)

print("编码：")
print(ids)

print()

print("解码：")
print(tokenizer.decode(ids))