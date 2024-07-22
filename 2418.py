# Sort the People

names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]


def sort_by_height(names, heights):
    combined = list(zip(names, heights))

    combined.sort(key=lambda x: x[1], reverse=True)

    sorted_names = [name for name, height in combined]

    return sorted_names


print(sort_by_height(names, heights))
