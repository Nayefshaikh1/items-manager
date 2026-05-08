from abc import ABC, abstractmethod


class ItemRepository(ABC):

    @abstractmethod
    def create(self, item):
        pass

    @abstractmethod
    def find(self, item_id):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def update(self, item):
        pass

    @abstractmethod
    def delete(self, item_id):
        pass