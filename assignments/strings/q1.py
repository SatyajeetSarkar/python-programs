''' “Interleaved Merge with Reversed Half” '''

# Interleaved Merge with Reversed Half

s1 = "abcccdd"
s2 = "123"

# reverse second string
new_s2 = s2[::-1]

i = 0
j = 0
new_str = []

# interleaving characters
while i < len(s1) and j < len(new_s2):
    new_str.append(s1[i])
    new_str.append(new_s2[j])
    i += 1
    j += 1

# add remaining characters from s1
while i < len(s1):
    new_str.append(s1[i])
    i += 1

# add remaining characters from new_s2
while j < len(new_s2):
    new_str.append(new_s2[j])
    j += 1

# final merged string
result = "".join(new_str)
print("Result:", result)
