import mymatrices


class Accountant:
    def __init__(self, name="Бухгалтер"):
        self._workers_transaction = {}
        self._name = name

    def record_worker(self, worker):
        if isinstance(worker, Datascientist):
            workers_list = self._workers_transaction.keys()
            if not (worker in workers_list):
                self._workers_transaction.update({worker: 0})
                print(f"{self._name} учёл работника {worker.name}")
                return True
            print(f"{worker.name} уже учтён")
            return True
        return False

    def give_salary(self, worker, amount):
        if isinstance(worker, Datascientist):
            workers_list = self._workers_transaction.keys()
            if worker in workers_list:
                self._workers_transaction.update({worker: amount})
                worker.take_salary(amount, self)
                print(f"{self._name} подтверждает, что {worker.name} получил ${amount}")
                return True
        print(f"{self._name} не знает {worker}")
        return False

    def __call__(self, worker, amount):
        if isinstance(worker, Datascientist):
            workers_list = self._workers_transaction.keys()
            if worker in workers_list:
                transaction = self._workers_transaction.get(worker)
                if transaction == amount:
                    self._workers_transaction.update({worker: 0})
                    print(f"{self._name} одобряет перечисление работнику {worker.name} ${amount}")
                    return True
                else:
                    print(f"{self._name} запрещает перечисление работнику {worker.name} ${amount}")
                    return False
            print(f"{self._name} не знает {worker}")
            return False
        print(f"{self._name} не знает {worker}")
        return False

    ##def __check_transaction(self):

    @property
    def name(self):
        return self._name

    @property
    def workers(self):
        workers = list(self._workers_transaction.keys())
        for i in range(len(workers)):
            workers[i] = workers[i].name
        return workers


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
            return False
        matrix1 = mymatrices.read_matrix(filename1)
        matrix2 = mymatrices.read_matrix(filename2)
        if not mymatrices.check_matrices(matrix1, matrix2):
            print(f"Не могу {(self.__dict.get(self.__work))[0]} матрицы")
            return False
        matrix_res = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1[0])):
                row.append((self.__dict.get(self.__work))[1](matrix1[i][j], matrix2[i][j]))
            matrix_res.append(row)
        mymatrices.matrix_out(matrix_res)
        return True

    def take_salary(self, acc, amount):
        if isinstance(acc, Accountant):
            if acc(self, amount):
                self.__money += amount
                print(f"{self.__name} получил ${amount}")
                return True
            print(f"{self.__name} не получил ${amount}")
            return False
        print(f"Нет такого бухгалтера {acc}")
        return False

    @property
    def name(self):
        return self.__name

    @property
    def wallet(self):
        return self.__money


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
