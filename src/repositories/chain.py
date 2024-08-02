from typing import ClassVar

from selenium.webdriver.remote.webdriver import WebDriver

from repositories.base import SeleniumRepository
from parsers.chain_parser import ChainParser
from schemas.chains import Chain


class ChainRepository(SeleniumRepository):
    url: ClassVar[str] = "https://defillama.com/chains"

    def __init__(self, driver: WebDriver, *args, **kwargs) -> None:
        chain_parser = ChainParser()
        super().__init__(driver, chain_parser, *args, **kwargs)

    def get(self, url: str = None, *args, **kwargs) -> list[Chain]:
        if url is None:
            url = self.url
        chains = super().get(url, *args, **kwargs)
        if chains and isinstance(chains[0], Chain):
            return chains

    def _get_data(self) -> WebDriver:
        return self.driver
