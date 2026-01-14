''' “Rotate & Shift-Merge Lists” '''

A = [1, 2, 3, 4, 5]
B = [10, 20, 30, 40, 50]

k = 2
rotated = []
result = [0] * len(A)

rotated = A[-k:] + A[:-k]

for i in range(len(A)):
    result[i] = rotated[i] + B[i]

print(rotated)
print(result)