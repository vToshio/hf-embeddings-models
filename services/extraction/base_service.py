from abc import ABC

class BaseService(ABC):
    @classmethod
    def extract(cls):
        raise NotImplementedError