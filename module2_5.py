def get_matrix(n, m, value):
    matrix = []
    matrix1 = []
    for i in range(m):
        matrix1.append(value)
    for j in range(n):
        matrix.append(matrix1)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
