# Напишите функцию для транспонирования матрицы

old_matrix = [[3, 5, 6],
              [2, 4, 7],
              [1, 8, 9]]


def matrix_transposition(matrix):
    trans_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]  # структура транспонированной матцы
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end=" ")
        print()


new_matrix = matrix_transposition(old_matrix)

print_matrix(old_matrix)
print('-' * 17)
print_matrix(new_matrix)
