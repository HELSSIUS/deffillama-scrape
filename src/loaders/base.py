import csv
import logging
from os import PathLike
from typing import Protocol, runtime_checkable
from abc import abstractmethod

from config import logger
from schemas.chains import Chain


@runtime_checkable
class Loader(Protocol):
    @abstractmethod
    def load(self, *args, **kwargs) -> None:
        """load data"""
        ...


class BaseLoader(Loader):
    def load(self, *args, **kwargs) -> None:
        logger.info(f"Uploading data to {self.__class__.__name__}")


class FileLoader(BaseLoader):
    def load(self, path: PathLike[str] | str, data: object | tuple | list, *args, **kwargs) -> None:
        """load data to file"""
        logger.info(f"Uploading data to {path} via {self.__class__.__name__}")
