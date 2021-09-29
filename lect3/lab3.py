import mymatrices


class Accountant:
    def __init__(self):
        self._workers_salaries = {}

    def give_salary(self, worker, amount):
        worker(self, amount)


class Datascientist:
    def __init__(self, name="Иван", money=25, work="что-то делать"):
        self.__name = name
        self.__money = money
        self.__work = work
        self.__dict = {'что-то делать': None,
                       'суммировать матрицы': ('сложить', lambda x, y: x + y),
                       'вычетать матрицы': ('вычесть', lambda x, y: x - y)}

    def do_work(self, filename1, filename2):
        if self.__work == "что-то делать":
            print("Я не знаю, что мне делать")
            return None
        matrix1 = mymatrices.read_matrix(filename1)
        matrix2 = mymatrices.read_matrix(filename2)
        if not mymatrices.check_matrices(matrix1, matrix2):
            print(f"Не могу {(self.__dict.get(self.__work))[0]} матрицы")
            return None
        matrix_res = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1[0])):
                row.append((self.__dict.get(self.__work))[1](matrix1[i][j], matrix2[i][j]))
            matrix_res.append(row)
        mymatrices.matrix_out(matrix_res)

    def __take_salary(self, x):
        self.__money += x

    def __call__(self, acc, amount):
        if isinstance(acc, Accountant):
            self.__take_salary(amount)



class Pupa(Datascientist):
    def __init__(self, name="Пупа", money=100):
        work = "суммировать матрицы"
        super().__init__(name, money, work)
        print(f"Датасайнтист {name} готов {work}")


class Lupa(Datascientist):
    def __init__(self, name="Лупа", money=10):
        work = "вычетать матрицы"
        super().__init__(name, money, work)
        print(f"Датасайнтист {name} готов {work}")


worker1 = Pupa("Алёша")
worker1.do_work("matrices\\1.txt", "matrices\\2.txt")
nachalnika = Accountant(worker1)
nachalnika.give_salary(worker1, 300)
worker2 = Lupa()
worker2.do_work("matrices\\1.txt", "matrices\\2.txt")
