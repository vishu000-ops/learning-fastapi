import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey there my name is vishu"

tokens = enc.encode(text)

print(tokens)

deco = enc.decode([25216, 1354, 922, 1308, 382, 323, 144320])
print(deco)

