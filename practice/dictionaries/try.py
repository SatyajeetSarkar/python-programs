''' Dictionaary filter '''

dic = { 'vega': 175, 'alden': 180, 'gentry': 165, 'Cox': 190 }

res = {}

for i in dic:
    if dic[i] > 170:
        res[i] = dic[i]

print(res)