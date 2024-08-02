import time
from decimal import Decimal

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from config import logger
from schemas.chains import Chain
from .base import Parser


class ChainParser(Parser):
    def parse(self, data: WebDriver, *args, **kwargs) -> list[Chain]:
        """ Parses table of chains """
        driver = data
        self.__goto_bottom(driver)
        try:
            source = driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/div/main/div[2]/div[4]")
            table = source.find_element(By.XPATH, "./div[2]")
        except NoSuchElementException as e:
            logger.error("Can not find chain table, error: ", e)
            return []

        chains = []
        try:
            rows = table.find_elements(By.XPATH, "./div")
        except NoSuchElementException as e:
            logger.error("Can not find chain rows, error: ", e)
            return []

        for row in rows:
            name = row.find_element(By.XPATH, "./div[1]/span/a").text
            protocols = row.find_element(By.XPATH, "./div[2]").text
            tvl = row.find_element(By.XPATH, "./div[7]").text
            chains.append(Chain(name, int(protocols), self.__parse_tvl(tvl)))
        return chains

    @staticmethod
    def __goto_bottom(driver: WebDriver) -> None:
        """ Scrolls to the bottom of the page to load more chains """
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeigh);")
            time.sleep(0.5)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                driver.set_window_size(1920, new_height)
                break
            last_height = new_height

    @staticmethod
    def __parse_tvl(tvl: str) -> Decimal:
        value_str = tvl.strip()

        if value_str.startswith('$'):
            value_str = value_str[1:]  # Remove leading dollar sign

        # Remove commas if present
        value_str = value_str.replace(',', '')

        # Check for suffixes and convert accordingly
        match value_str[-1]:
            case 'b':
                return Decimal(value_str[:-1]) * Decimal("1_000_000_000")
            case 'm':
                return Decimal(value_str[:-1]) * Decimal("1_000_000")
            case _:
                return Decimal(value_str)
