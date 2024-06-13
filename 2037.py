# Minimum Number of Moves to Seat Everyone

seats = [4, 1, 5, 9]
students = [1, 3, 2, 6]


def prob(lst1, lst2):
    lst3 = sorted(lst1)
    lst4 = sorted(lst2)

    j = 0
    count = 0

    for i in lst3:
        count += abs(i-lst4[j])
        j += 1
    return count


print(prob(seats, students))
