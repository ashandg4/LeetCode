#  Minimum Number of Chairs in a Waiting Room

s = "ELEELEELLL"
people = 0
chairs = 0

for char in s:
    if char == 'E':
        people += 1

    elif char == 'L':
        people -= 1

    chairs = max(chairs, people)

print(chairs)
