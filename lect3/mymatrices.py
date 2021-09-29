def read_matrix(f_name):
    matrix = []
    with open(f_name) as f:
        row = f.readline()
        row = line_parse(row)
        while len(row) != 0:
            matrix.append(row)
            row = f.readline()
            row = line_parse(row)
    return matrix


def line_parse(line):
    res = []
    sign = 1
    while len(line) > 0:
        char = line[0]
        line = line[1:]
        if char.isnumeric():
            num = int(char)
            if len(line) > 0:
                char = line[0]
                line = line[1:]
            else:
                char = "end"
            while char.isnumeric():
                num = num * 10 + int(char)
                char = line[0]
                line = line[1:]
                if len(line) == 0:
                    break
            res.append(num * sign)
            sign = 1
        elif char == '-':
            sign = -1
    return res


def check_matrices(matrix_a, matrix_b):
    col_a = len(matrix_a[0])
    for i in range(len(matrix_a)):
        if len(matrix_a[i]) != col_a:
            print('Неверный формат первой матрицы')
            return False
    row_b = len(matrix_b)
    row_a = len(matrix_a)
    col_b = len(matrix_b[0])
    for i in range(row_b):
        if len(matrix_b[i]) != col_b:
            print('Неверный формат второй матрицы')
            return False
    if col_b != col_a or row_a != row_b:
        print('Матрицы несовместимы для')
        return False
    return True


def matrix_out(matrix):
    ln = len(matrix[0])
    for i in range(len(matrix)):
        for j in range(ln):
            print(str((matrix[i])[j]), end=' ')
        print()
