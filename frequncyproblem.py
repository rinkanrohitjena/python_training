

line = "this is  a simple line"


char_freq = {}
for char in line:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
print(sorted(char_freq.items()))
