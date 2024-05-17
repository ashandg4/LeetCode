dict1 = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}
digits = input("Enter any number (2-9): ")
list1 = ['']

if not digits:
    print([])
else:
    for digit in digits:
        list2 = []
        for char in dict1[digit]:
            for element in list1:
                list2 = list2+[element+char]
        list1 = list2
    print(list1)
