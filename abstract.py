from abc import ABC, abstractmethod
class Phone(ABC):
    @abstractmethod
    def func(self):
        pass
obj=Phone()    
