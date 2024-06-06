# Hand of Straights

from collections import Counter
hand = [1, 2, 3, 4, 5]
groupSize = 4

cnt = Counter(hand)         # tells the frequency of each element
for i in sorted(hand):
    if cnt[i]:
        for x in range(i, i + groupSize):
            if cnt[x] == 0:
                print(False)
            cnt[x] -= 1
            if cnt[x] == 0:
                cnt.pop(x)
print(True)
