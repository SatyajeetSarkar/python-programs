''' “Longest Increasing-Digit-Sum Substring (Contiguous)” '''

s = "12 3 45 9 10 2 100"

nums = s.split()
digit_sums = []

for n in nums:
    total = 0

    for ch in n:
        total += ord(ch)-48

    digit_sums.append(total)

max_len = 1
max_start = 0

curr_len = 1
curr_start = 0

for i in range(1, len(digit_sums)):
    if digit_sums[i] > digit_sums[i - 1]:
        curr_len += 1
    else:
        if curr_len > max_len:
            max_len = curr_len
            max_start = curr_start
            
        curr_len = 1
        curr_start = i

if curr_len > max_len:
    max_len = curr_len
    max_start = curr_start

result = nums[max_start : max_start + max_len]

print("Longest Increasing-Digit-Sum Subsequence:", " ".join(result))
print("Length:", max_len)
