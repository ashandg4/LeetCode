# Find the Child Who Has the Ball After K Seconds

n = 5
k = 6

pos = 0
dir = 1

for i in range(k):
    pos += dir

    if pos == 0 or pos == n - 1:
        dir *= -1

print(pos)
