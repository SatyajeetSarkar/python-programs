''' “Balanced-String Test (All chars present)” '''

a = "string123"
b = "stringg"

balance = []
miss_char = []

for s in a:
    if s in b and s not in balance:
        balance.append(s)
    else:
        miss_char.append(s)

if balance:
    print(f"True. \nMissing Character: {' '.join(miss_char)}")
else:
    print('False.')