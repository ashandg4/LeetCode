# Find The First Player to win K Games in a Row

import queue
skills = [4, 2, 6, 3, 9]
k = 2

n = len(skills)
players = queue.Queue()

for i in range(n):
    players.put(i)

current_player = players.get()
cons_wins = 0

while cons_wins < k:
    chal = players.get()

    if skills[current_player] > skills[chal]:
        cons_wins += 1
        players.put(chal)
    else:
        cons_wins = 1
        players.put(current_player)
        current_winner = chal
print(current_winner)
