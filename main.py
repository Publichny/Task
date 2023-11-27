# satr = input("Satrni kiriting: ")
# middle = len(satr) // 2
# print(satr[middle-1:middle+2])


# str1 = 'Ona'
# print("Original String is", str1)

# res = str1[0] + str1[len(str1) // 2] + str1[-1]

# print("New String:", res)



str1 = "PyNaTive"

lower = []
upper = []

for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)

sorted_str = ''.join(lower + upper)
print('Result:', sorted_str)