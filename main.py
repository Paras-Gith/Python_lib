import tiktoken


enc = tiktoken.encoding_for_model('gpt-4o')

text = "Hey There! My name is Paras Nainwal"
tokens = enc.encode(text)

print("Token", tokens)


# this is the OUTPUT of text variable :Token [25216, 3274, 0, 3673, 1308, 382, 145961, 478, 524, 22314]

decoded = enc.decode([25216, 3274, 0, 3673, 1308, 382, 145961, 478, 524, 22314])
print("Decoded", decoded)


#this is the OUPUT of the decoded: Decoded Hey There! My name is Paras Nainwal