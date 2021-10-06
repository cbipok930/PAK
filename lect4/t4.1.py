import numpy as np


arr_size = 90
arr = np.random.randint(10, size=arr_size)
print(f"Входной массив:\n {arr}\n")
freqs = np.unique(arr, return_counts=True)
arr_to_sort = np.array((freqs[0], freqs[1]), dtype=tuple)
arr_to_sort = np.transpose(arr_to_sort, axes=None)
final = arr_to_sort[np.argsort(arr_to_sort[:, 1])]
final = np.transpose(final, axes=None)
print(f'Элементы массива, отсортированные по частоте: {list(final[0])[::-1]}\n')
