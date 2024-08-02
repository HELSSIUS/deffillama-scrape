import logging
import os
import re

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=os.getenv("LOG_LEVEL", "INFO"),
)
logger = logging.getLogger(__name__)


class ChainScheduleConfig:
    """ Configuration for scheduler """

    def __init__(self):
        self.str_interval = os.getenv("CHAIN_SCHEDULE_INTERVAL", "5m")
        self.interval = self.parse_interval()

    def parse_interval(self) -> int:
        """ Parse interval string to seconds """
        each = self.str_interval
        regex = r"(\d+M)?(\d+d)?(\d+h)?(\d+m)?(\d+s)?"
        match = re.match(regex, each)
        if not match:
            raise ValueError("Invalid EACH format")

        months = int(match.group(1)[:-1]) if match.group(1) else 0
        days = int(match.group(2)[:-1]) if match.group(2) else 0
        hours = int(match.group(3)[:-1]) if match.group(3) else 0
        minutes = int(match.group(4)[:-1]) if match.group(4) else 0
        seconds = int(match.group(5)[:-1]) if match.group(5) else 0

        total_seconds = months * 30 * 24 * 3600 + days * 24 * 3600 + hours * 3600 + minutes * 60 + seconds
        return total_seconds
