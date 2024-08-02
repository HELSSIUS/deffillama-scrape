from dataclasses import dataclass
from decimal import Decimal
from typing import Iterable

from .base import CSVAble


@dataclass
class Chain(CSVAble):
    name: str
    protocols: int
    tvl: Decimal

    def get_csv_headers(self) -> tuple[str, ...]:
        return tuple(self.__annotations__)

    def to_csv_row(self) -> Iterable:
        return [self.name, self.protocols, str(self.tvl)]

    @classmethod
    def from_csv_row(cls, items: list) -> "Chain":
        return cls(items[0], int(items[1]), Decimal(items[2]))
