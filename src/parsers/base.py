from abc import abstractmethod
from typing import Protocol, runtime_checkable


@runtime_checkable
class Parser(Protocol):
    @abstractmethod
    def parse(self, data: object, *args, **kwargs) -> object:
        ...


@runtime_checkable
class AsyncParser(Protocol):
    @abstractmethod
    async def async_parse(self, data: object, *args, **kwargs) -> object:
        ...


class CombinedParser(Parser, AsyncParser):
    def parse(self, data: object, *args, **kwargs) -> object:
        pass

    async def async_parse(self, data: object, *args, **kwargs) -> object:
        pass
