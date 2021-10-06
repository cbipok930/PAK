import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("r_path", type=str, help='Путь к файлу с реальными данными')
parser.add_argument("i_path", type=str, help='Путь к файлу с синтетическими данными')
args = parser.parse_args()
real_p = os.path.abspath(args.r_path)
im_p = os.path.abspath(args.im_path)
