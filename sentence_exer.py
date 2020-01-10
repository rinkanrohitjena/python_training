sentence = "this is a very simple statement"
sentence_dict = {}

for char in sentence:
    if char in sentence_dict:
        sentence_dict[char] += 1
    else:
        sentence_dict[char] = 1
print(sentence_dict)
