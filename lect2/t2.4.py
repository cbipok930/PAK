import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("synonyms_file", type=str, help='Файл со списком пар слово-синоним"')
args = parser.parse_args()
fi_p = args.synonyms_file
os.chdir(os.path.dirname(os.path.abspath(fi_p)))
f_name = os.path.basename(fi_p)
file = open(f_name)
synonyms_dict = {}
pair_string = file.readline()
while len(pair_string) != 0:
    key_word = ''.join(list(pair_string)[:(pair_string.find(' '))])
    val_word = ''.join(list(pair_string)[(pair_string.find(' ') + 1):len(pair_string) - 1])
    newdict = {key_word: val_word}
    synonyms_dict.update(newdict)
    pair_string = file.readline()
file.close()
print('Введите строку')
string = input()
string_lst = string.split(" ")
l = len(string_lst)
for i in range(l):
    word = ''.join(string_lst[i])
    sep = iter([',', '.', '!', '?'])
    for ii in sep:
        j = word.find(ii)
        while j > -1:
            wordl = list(word)
            wordl.remove(wordl[j])
            word = ''.join(wordl)
            j = word.find(ii)
    string_lst[i] = word
for i in range(l):
    key = string_lst[i]
    val = synonyms_dict.get(key.lower())
    if val is not None:
        string_lst[i] = val
        string = string.replace(key, val, 1)
    else:
        for j in range(len(synonyms_dict.keys())):
            pair = list(synonyms_dict.items())[j]
            if key == pair[1]:
                val = pair[0]
                string = string.replace(key, val, 1)
                break
print(string)
