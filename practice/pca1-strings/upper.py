str = 'Ter'
new_str = ''

for ch in str:
    if ord(ch) >= 97: 
        new_str += chr(ord(ch) - 32)
    else:
        new_str += chr(ord(ch) + 32)

print(new_str)