'''Write a program to capitalize the first and last character of each word in a string'''

s = "hello world"

words = []
w = ''

# Split function
for ch in s:
    if ch == ' ':
        words.append(w)
        w = ''
    else:
        w += ch
words.append(w)

# words = s.split()

result = []

for w in words:
    if len(w) == 1:
        result.append(chr(ord(w)-32))
    else:
        new_w = chr(ord(w[0])-32) + w[1:-1] + chr(ord(w[-1])-32)
        result.append(new_w)

print(" ".join(result))


