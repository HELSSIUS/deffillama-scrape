from abc import abstractmethod
from typing import Protocol, runtime_checkable


@runtime_checkable
class Parser(Protocol):
    """Parser interface"""

    @abstractmethod
    def parse(self, data: object, *args, **kwargs) -> object:
        ...


@runtime_checkable
class AsyncParser(Protocol):
    """AsyncParser interface"""

    @abstractmethod
    async def async_parse(self, data: object, *args, **kwargs) -> object:
        ...
