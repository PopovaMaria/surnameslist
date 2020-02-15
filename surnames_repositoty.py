from input_stategies import  IInputStrategy


class CantPopItem(Exception):
    pass


class CantChangeItem(Exception):
    pass


class SurnameRepository:
    def __init__(self, input_strategy: IInputStrategy):
        self._surnames = []
        self._input_strategy = input_strategy

    def add(self):
        surname = self._input_strategy.read_surname()
        self._surnames.append(surname)

    def pop(self):
        indexes = self._input_strategy.read_indexes()
        try:
            for index in indexes:
                self._surnames.pop(index)
        except IndexError as e:
            raise CantPopItem from e

    def change(self):
        index = self._input_strategy.read_index()
        surname = self._input_strategy.read_surname()
        try:
            self._surnames[index] = surname
        except IndexError as e:
            raise CantChangeItem from e

    def __str__(self):
        return f'Фамилии: {self._surnames}'