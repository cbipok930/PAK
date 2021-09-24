import argparse
import os


def read_strings_from_file(s_list, name):
    file = open(name)
    string = file.readline()
    while len(string) != 0:
        if string[len(string) - 1] == '\n':
            string = ''.join(list(string)[:len(string) - 1])
        s_list.append(string)
        string = file.readline()
    file.close()
    return s_list


parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help='Путь к файлу"')
args = parser.parse_args()
fi_p = args.file
os.chdir(os.path.dirname(os.path.abspath(fi_p)))
f_name = os.path.basename(fi_p)
strings = []
strings = read_strings_from_file(strings, f_name)
str_cnt = len(strings)
word_cnt = 0
letters_cnt = 0
words = []
for i in range(str_cnt):
    string = strings.pop(0)
    while len(string) > 0:
        space_ptr = string.find(' ')
        if space_ptr > -1:
            word = ''.join(list(string)[:space_ptr])
            string = ''.join(list(string)[space_ptr + 1: len(string)])
        else:
            word = string
            string = []
        if len(word) > 0:
            words.append(word)
            word_cnt += 1
for i in range(word_cnt):
    word = list(words.pop(0))
    while len(word) > 0:
        letters_cnt += 1
        word.pop(0)
print("Строк:", str_cnt, '\n', "Слов:", word_cnt, '\n', "Букв:", letters_cnt)

