# Count Pairs That Form a Complete Day I

hours = [12, 12, 30, 24, 24]

remainder_freq = {}
total_pairs = 0

for time in hours:
    remainder = time % 24
    x = (24 - remainder) % 24

    if x in remainder_freq:
        total_pairs += remainder_freq[x]

    remainder_freq[remainder] = remainder_freq.get(
        remainder, 0) + 1

print(total_pairs)
