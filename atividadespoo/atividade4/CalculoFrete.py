from abc import ABC, abstractmethod

class Frete(ABC):
    @abstractmethod
    def valor(self,): pass