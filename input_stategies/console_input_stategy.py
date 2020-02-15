from . import *
from gettext import gettext as _


class ConsoleInputStrategy(IInputStrategy):

    def read_surname(self) -> str:
        surname = input(_('Введите фамилию'))
        return surname

    def read_index(self) -> int:
        index = input(_('Введите индекс'))
        try:
            return int(index)
        except ValueError:
            return self.read_index()

    def read_indexes(self) -> List[int]:
        indexes = input(_('Введите список цифр через пробел'))
        try:
            indexes = indexes.split(' ')
            indexes = [int(index) for index in indexes]
            return indexes
        except ValueError:
            return self.read_indexes()
