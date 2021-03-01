
# Create 2 matrix
def input_matrixes():
    n_of_a, m_of_a = input("Enter size of first matrix: ").split()
    print("Enter first matrix:")
    matrix_1 = [input().split() for i in range(int(n_of_a))]
    n_of_b, m_of_b = input("Enter size of second matrix: ").split()
    print("Enter second matrix:")
    matrix_2 = [input().split() for i in range(int(n_of_b))]
    return matrix_1, matrix_2


def print_matrix(matrix):
    print('The result is:')
    for i in matrix:
        print(*i)


# Create 1 matrix
def input_matrix():
    n_of_a, m_of_a = input('Enter size of matrix: ').split()
    print('Enter matrix:')
    matrix_1 = [input().split() for i in range(int(n_of_a))]
    return matrix_1


# Add first matrix to second matrix
def list_add(list_1, list_2):
    result_temp = []
    if '.' in list_1[0]:
        for a, b in zip(list_1, list_2):
            result_temp.append(str(float(a) + float(b)))
    else:
        for a, b in zip(list_1, list_2):
            result_temp.append(str(int(a) + int(b)))
    return result_temp


# multiply matrix
def multiply_matrix(parts_of_matrix, multiplier):
    return [str(int(i) * multiplier) for i in parts_of_matrix]


# multiply float matrix
def multiply_matrix_float(parts_of_matrix, multiplier):
    return [str(float(i) * multiplier) for i in parts_of_matrix]


# multiply matrix for constanta
def multiply_matrix_by_constant():
    matrix = input_matrix()
    constanta = input('Enter constant: ')
    if '.' in constanta:
        result = [multiply_matrix_float(i, float(constanta)) for i in matrix]
    else:
        result = [multiply_matrix(i, int(constanta)) for i in matrix]
    print_matrix(result)


# add two matrix
def add_matrices():
    matrix_1, matrix_2 = input_matrixes()
    n_of_a, m_of_a = len(matrix_1[0]), len(matrix_1)
    n_of_b, m_of_b = len(matrix_2[0]), len(matrix_2)

    if n_of_a == n_of_b and m_of_a == m_of_b:
        result = []
        for i, j in zip(matrix_1, matrix_2):
            result.append(list_add(i, j))
        print_matrix(result)
    else:
        print('ERROR')


# multiply two matrix
def multiply_matrices():
    matrix_1, matrix_2 = input_matrixes()
    m_of_a = len(matrix_1[0])
    n_of_b = len(matrix_2)
    if m_of_a != n_of_b:
        print("The operation cannot be performed.")
    else:
        if '.' in matrix_1[0][0]:
            result = [[sum(float(a) * float(b) for a, b in zip(X_row, Y_col)) for Y_col in zip(*matrix_2)] for X_row in
                      matrix_1]
        else:
            result = [[sum(int(a) * int(b) for a, b in zip(X_row, Y_col)) for Y_col in zip(*matrix_2)] for X_row in
                      matrix_1]
        print_matrix(result)


def transpose_matrix():
    print('1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line')
    second_choice = input()
    if second_choice == '1':
        transpose_matrix_by_main_diagonal()
    elif second_choice == '2':
        transpose_matrix_by_side_diagonal()
    elif second_choice == '3':
        transpose_along_vertical_line()
    elif second_choice == '4':
        transpose_along_horizontal_line()


def transpose_matrix_by_main_diagonal():
    matrix = input_matrix()
    n, m = len(matrix[0]), len(matrix)
    for i in range(m):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print_matrix(matrix)


def transpose_matrix_by_side_diagonal():
    matrix = input_matrix()
    n, m = len(matrix[0]), len(matrix)
    for i in range(n):
        for j in range(m - i):
            matrix[i][j], matrix[n - j - 1][m - i - 1] = matrix[n - j - 1][m - i - 1], matrix[i][j]
    print_matrix(matrix)


def transpose_along_vertical_line():
    matrix = input_matrix()
    transposed_matrix = []
    for i in matrix:
        transposed_matrix.append(i[::-1])
    print_matrix(transposed_matrix)


def transpose_along_horizontal_line():
    matrix = input_matrix()
    transposed_matrix = matrix[::-1]
    print_matrix(transposed_matrix)


def determinant(matrix):
    if len(matrix) == len(matrix[0]):
        if len(matrix) == 2:
            return int(matrix[0][0]) * int(matrix[1][1]) - int(matrix[0][1]) * int(matrix[1][0])
        elif len(matrix) == 1:
            return int(matrix[0][0])
        else:
            return sum(
                [((-1) ** n) * int(matrix[0][n]) * determinant(slice_matrix(matrix, n)) for n in range(len(matrix))])
    else:
        return None


def determinant_float(matrix):
    if len(matrix) == len(matrix[0]):
        if len(matrix) == 2:
            return float(matrix[0][0]) * float(matrix[1][1]) - float(matrix[0][1]) * float(matrix[1][0])
        elif len(matrix) == 1:
            return float(matrix[0][0])
        else:
            return sum([((-1) ** n) * float(matrix[0][n]) * determinant_float(slice_matrix(matrix, n)) for n in
                        range(len(matrix))])
    else:
        return None


def slice_matrix(matrix, slice_index):
    return [row[0:slice_index] + row[slice_index + 1:] for row in matrix[1:]]


def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]


def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("Matrix is not invertible")
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a


def inverse():
    temp = input_matrix()
    if '.' in temp[0][1]:
        matrix = [[float(j) for j in i] for i in temp]
    else:
        matrix = [[int(j) for j in i] for i in temp]
    tmp = [[] for _ in matrix]
    for i,row in enumerate(matrix):
        assert len(row) == len(matrix)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(matrix)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])

    print_matrix(ret)


while True:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
    choice = input('Your choice: ')
    if choice == '1':
        add_matrices()
    elif choice == '2':
        multiply_matrix_by_constant()
    elif choice == '3':
        multiply_matrices()
    elif choice == '4':
        transpose_matrix()
    elif choice == '5':
        matrixx = input_matrix()
        if '.' in matrixx[0][0]:
            print(determinant_float(matrixx))
        else:
            print(determinant(matrixx))
    elif choice == '6':
        inverse()
    elif choice == '0':
        exit(0)
