from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    @abstractmethod
    def get_user(self, id):
        pass

