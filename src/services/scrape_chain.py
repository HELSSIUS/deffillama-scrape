import schedule
import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.remote.webdriver import WebDriver
from config import ChainScheduleConfig, logger
from loaders.csv_loader import CSVLoader
from repositories.chain import ChainRepository
from services.base import Service


class ScrapeChainService(Service):
    @staticmethod
    def serve(driver_type: type[WebDriver] = Chrome, options: ChromeOptions = ChromeOptions()) -> None:
        with driver_type(options=options) as driver:
            chain_repository = ChainRepository(driver)
            chain = chain_repository.get()

            csv_loader = CSVLoader()
            csv_loader.load("chains.csv", chain)

    def run(self, config: ChainScheduleConfig, driver: type[WebDriver] = Chrome,
            options: ChromeOptions = ChromeOptions()) -> None:
        # Convert interval to seconds and schedule the task
        interval_seconds = config.parse_interval()
        schedule.every(interval_seconds).seconds.do(self.serve, driver_type=driver, options=options)

        logger.info(f"ScrapeChainService started with id: {id(self)}")
        try:
            while True:
                schedule.run_pending()
                time.sleep(1)  # Sleep to prevent high CPU usage
        except KeyboardInterrupt:
            logger.warning("ScrapeChainService stopped by KeyboardInterrupt")
        finally:
            self.stop()  # Ensure resources are cleaned up

    def stop(self) -> None:
        logger.info(f"ScrapeChainService stopped with id: {id(self)}")

    def __enter__(self, config: ChainScheduleConfig, driver: type[WebDriver] = Chrome,
                  options: ChromeOptions = ChromeOptions(), *args, **kwargs) -> None:
        self.run(config, driver, options)
