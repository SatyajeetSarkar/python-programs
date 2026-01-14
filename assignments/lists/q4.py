''' “Sliding Window Average & Variance Tracker” '''
data = [5, 7, 3, 9, 12, 4, 6]
k = 3

result = []

for i in range(len(data) - k + 1):
    window = data[i : i + k]
    
    avg = sum(window) / k

    var = 0
    for x in window:
        var += (x-avg)**2
    var = var/k
    
    result.append((avg,var))

print(result)
