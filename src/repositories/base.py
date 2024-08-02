from abc import abstractmethod, ABC
from typing import Protocol, ClassVar

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from config import logger
from parsers.base import Parser


class Repository(Protocol):
    """Can be used to fetch data from different sources in different ways"""

    @abstractmethod
    def get(self, url: str, *args, **kwargs) -> object | list:
        """Get data from repository"""
        ...


class BaseRepository(Repository, ABC):
    url: ClassVar[str] = None

    def __init__(self, parser: Parser, *args, **kwargs) -> None:
        self.__is_class_var_set()
        super().__init__(*args, **kwargs)
        self.parser = parser

    def get(self, url: str = None, *args, **kwargs) -> object | list:
        logger.info(f"Get data from {self.__class__.__name__} with url: {url}")
        return self.parser.parse(self._get_data())

    @abstractmethod
    def _get_data(self) -> object:
        raise NotImplementedError

    @classmethod
    def __is_class_var_set(cls) -> None:
        if cls.url is None:
            raise ValueError("Class variable url is not set. Please set it first")


class SeleniumRepository(BaseRepository, ABC):
    """Can be used to fetch data from dynamic resources"""

    def __init__(self, driver: WebDriver, parser: Parser, *args, **kwargs) -> None:
        super().__init__(parser, *args, **kwargs)
        self.driver = driver

    def get(self, url: str = None, *args, **kwargs) -> object | list:
        self.driver.get(url)
        return super().get(url, *args, **kwargs)
