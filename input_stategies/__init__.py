from typing import List
from abc import ABC, abstractmethod


class IInputStrategy(ABC):
    @abstractmethod
    def read_surname(self) -> str:
        pass

    @abstractmethod
    def read_index(self) -> int:
        pass

    @abstractmethod
    def read_indexes(self) -> List[int]:
        pass
