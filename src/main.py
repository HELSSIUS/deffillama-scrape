from selenium.webdriver import ChromeOptions

from config import ChainScheduleConfig, PROXY
from services.scrape_chain import ScrapeChainService


def main():
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 "
        "Safari/537.36"
    )
    if PROXY:
        options.add_argument(f"--proxy-server={PROXY}")

    service = ScrapeChainService()
    service.run(config=ChainScheduleConfig(), options=options)


if __name__ == "__main__":
    main()
