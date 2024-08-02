from abc import abstractmethod, ABC


class Service(ABC):
    """ Base class for all services """

    def __enter__(self, *args, **kwargs):
        self.run(*args, **kwargs)

    def __exit__(self, exc_type, exc_val, exc_tb, *args, **kwargs):
        self.stop(*args, **kwargs)

    @abstractmethod
    def run(self, *args, **kwargs) -> None:
        raise NotImplementedError

    @abstractmethod
    def stop(self, *args, **kwargs) -> None:
        raise NotImplementedError
