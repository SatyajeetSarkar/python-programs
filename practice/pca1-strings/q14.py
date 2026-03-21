'''Write a program to odd Frequency Characters'''

s = "ougiugiygi"

odd_chars = {}

for ch in s:
    if s not in odd_chars and s.count(ch) % 2 != 0:
        odd_chars[ch] = s.count(ch)

print(odd_chars)
