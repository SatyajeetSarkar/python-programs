'''Write a program uppercase Half String.'''

s = "Random"
n = len(s)
half = n // 2   # first half length
    
result = ""
    
for i in range(n):
    ch = s[i]
        
    if i < half and 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)
    else:
        result += ch

print(result)

'''
def to_upper(s):
    result = ""
    for ch in s:
        if 'a' <= ch <= 'z':   # check lowercase
            result += chr(ord(ch) - 32)
        else:
            result += ch
    return result

# Example
print(to_upper("hello World"))   # HELLO WORLD
'''

'''
def to_lower(s):
    result = ""
    for ch in s:
        if 'A' <= ch <= 'Z':   # check uppercase
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result

# Example
print(to_lower("HELLO World"))   # hello world
'''
