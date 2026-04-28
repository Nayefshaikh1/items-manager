from abc import ABC, abstractmethod

class StorageBase(ABC):

    @abstractmethod
    def save_items(self, items):
        pass

    @abstractmethod
    def load_items(self):
        pass