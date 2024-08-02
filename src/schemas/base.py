from abc import abstractmethod
from typing import Protocol, runtime_checkable, Iterable


@runtime_checkable
class CSVAble(Protocol):
    @abstractmethod
    def get_csv_headers(self) -> tuple:
        ...

    @abstractmethod
    def to_csv_row(self) -> Iterable:
        ...

    @classmethod
    @abstractmethod
    def from_csv_row(cls, items: list) -> object:
        ...


@runtime_checkable
class JSONAble(Protocol):
    @abstractmethod
    def to_json(self) -> dict[str, object]:
        ...

    @abstractmethod
    def from_json(self, data: str) -> object:
        ...
