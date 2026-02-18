'''
5. Count Consecutive Increase Blocks”
● Problem statement:Input a sequence of 8 integers, count how many blocks of
consecutive increasing numbers exist. A block is defined as one or more numbers such
that each number after the first in the block is strictly greater than its predecessor. For
example [2, 3, 5, 1, 2, 3, 3, 4] has: first block [2,3,5], then second block [1,2,3], skip the 3 to
3 since not strictly greater, then third block [3,4]. So the answer would be 3. Also print the
length of the longest block.
● Input: A list of integers (length ≥ 1).
● Output: Two integers: number of increasing-blocks, and length of the longest block.
● Processing logic:
■ Initialize block_count = 0, current_length = 1, longest = 1.
■ Loop from second element to end: compare current with previous.
○ If current > previous: increment current_length.
○ Else: end of block → increment block_count; update longest =
max(longest, current_length); reset current_length = 1.

■ After loop, handle the last block (increment block_count; update longest).
■ Print block_count and longest.
'''

# Count Consecutive Increase Blocks (with block data shown)

n = int(input("Enter number of terms: "))

count = 1
no_block = 1
max_block_length = 1
block_length = 1

blocks = ""            # will store all block info as a single string
current_block = ""     # stores current block values

while count <= n:
    num = int(input("Enter a number: "))

    if count == 1:
        value = num
        current_block = str(num)  # start first block
    else:
        if num > value:
            block_length += 1
            current_block += " " + str(num)
        else:
            # end of current block
            blocks += f"[{current_block}], "
            if block_length > max_block_length:
                max_block_length = block_length
            # start new block
            no_block += 1
            block_length = 1
            current_block = str(num)
        value = num
    count += 1

# handle last block
blocks += f"[{current_block}]"
if block_length > max_block_length:
    max_block_length = block_length

# output
print("\n--- Blocks Found ---")
print(blocks)
print(f"Number of increasing blocks: {no_block}")
print(f"Length of the longest block: {max_block_length}")

