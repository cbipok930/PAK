import os
import argparse


def read_matrices(f_name):
    """
    Reads matrices from file

    Parameters
    ----------
    f_name: str
        Path to file where read from

    Returns
    -------
    matrix1, matrix2 : list<str>
        Matrices from file
    """
    matrix1 = []
    matrix2 = []
    with open(f_name) as f:
        for i in range(2):
            row = f.readline()
            row = line_parse(row)
            while len(row) != 0:
                if i == 0:
                    matrix1.append(row)
                else:
                    matrix2.append(row)
                row = f.readline()
                row = line_parse(row)
    return matrix1, matrix2


def line_parse(line):
    """
    Makes list of row's elements from string

    Parameters
    ----------
    line: str
        String

    Returns
    -------
    res : list
        Matrix's row
    """
    res = []
    sign = 1
    while len(line) > 0:
        char = line[0]
        line = line[1:]
        if char.isnumeric():
            num = int(char)
            char = line[0]
            line = line[1:]
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


def mult_matrices(matrix1, matrix2):
    """
    Multiplies matrices

    Parameters
    ----------
    matrix1, matrix2: list
        Matrices where each as list of lists

    Returns
    -------
    matrix_r : list
        Result matrix
    """
    n = len(matrix1)
    m = len(matrix2[0])
    ll = len(matrix2)
    matrix_r = []
    for i in range(n):
        row = []
        for j in range(m):
            c = 0
            for k in range(ll):
                c += matrix1[i][k] * matrix2[k][j]
            row.append(c)
        matrix_r.append(row)
    return matrix_r


def check_matrices(matrix_a, matrix_b):
    """
    Checks if matrices may be multiplied
    Prints message in case of they can't be

    Parameters
    ----------
    matrix_a, matrix_b: list<list>
        Matrices where each as list of lists

    Returns
    -------
    1: If failed
    0: If OK
    """
    col_a = len(matrix_a[0])
    for i in range(len(matrix_a)):
        if len(matrix_a[i]) != col_a:
            print('Неверный формат первой матрицы')
            return 1
    row_b = len(matrix_b)
    if row_b != col_a:
        print('Матрицы несовместимы')
        return 1
    col_b = len(matrix_b[0])
    for i in range(row_b):
        if len(matrix_b[i]) != col_b:
            print('Неверный формат второй матрицы')
            return 1
    return 0


def matrix_out(matrix, f_name):
    """
    Writes matrix in file

    Parameters
    ----------
    matrix: list<list>
        Matrix to write
    f_name: path to output file

    """
    with open(f_name, 'w') as f:
        l = len(matrix[0])
        for i in range(len(matrix)):
            for j in range(l):
                f.write(str((matrix[i])[j]))
                f.write(' ')
            f.write("\n")


def main():
    """
    Reads matrix from file
    Multiplies them
    Writes result of multiplication in another file

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("i_path", type=str, help='Путь к файлу с матрицами')
    parser.add_argument("o_path", type=str, help='Путь к файлу с результирующей матрицей')
    args = parser.parse_args()
    input_p = os.path.abspath(args.i_path)
    output_p = os.path.abspath(args.o_path)
    matrix_first, matrix_sec = read_matrices(input_p)
    if check_matrices(matrix_first, matrix_sec) == 1:
        return 1
    matrix_fin = mult_matrices(matrix_first, matrix_sec)
    matrix_out(matrix_fin, output_p)
    return 0


main()
