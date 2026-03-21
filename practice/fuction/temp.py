'''
def check_range(target, low, high):
    return low <= target <= high

print(check_range(5, 2, 10))
'''

import re
print(re.findall('aa[cde]?', 'aacde aa aadcde'))