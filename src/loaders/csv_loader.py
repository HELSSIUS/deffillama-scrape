import csv
import logging
from os import PathLike
from schemas.base import CSVAble
from .base import FileLoader


class CSVLoader(FileLoader):
    def load(self, path: PathLike[str] | str, data: tuple[CSVAble] | list[CSVAble], *args,
             with_headers: bool = False, **kwargs) -> None:
        try:
            super().load(path, data, *args, **kwargs)
            with open(path, "w", newline="") as f:
                writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
                if with_headers:
                    writer.writerow(data[0].get_csv_headers())
                for chain in data:
                    writer.writerow(chain.to_csv_row())
        except OSError as e:
            logging.error(e)
