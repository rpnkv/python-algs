two_dim_array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

for arr in two_dim_array:
    for i in arr:
        print(i)


for i in range(len(two_dim_array)):
    for j in range(len(two_dim_array[i])):
        print(f"{i} {j} {two_dim_array[i][j]}")