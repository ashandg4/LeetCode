# Three Consecutive Odds

arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]


def f(arr):
    cnt = 0
    for i in arr:
        if i & 1:
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            return True
    return False


print(f(arr))
