import os
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("i_path", type=str, help='Путь к файлу с матрицами')
    parser.add_argument("o_path", type=str, help='Путь к файлу с результирующей матрице')
    args = parser.parse_args()
    input_p = os.path.abspath(args.i_path)
    output_p = os.path.abspath(args.o_path)
    matrix_first = []
    matrix_sec = []
    with open(input_p) as f:
        row = f.readline()
        while len(row) != 0:
            matrix_first.append()
    return 0


main()
