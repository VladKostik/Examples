from abc import ABC, abstractmethod


class IGun(ABC):
    @abstractmethod
    def shooting(self):
        """Describes shooting the gun"""
        pass

    @abstractmethod
    def loading(self):
        """Describes loading the gun"""
        pass