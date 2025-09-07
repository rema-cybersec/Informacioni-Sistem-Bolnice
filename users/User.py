from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def __init__(self, username: str, password: str):
        pass
    @abstractmethod
    def GetSecretKey(self) -> str:
        pass
    @abstractmethod
    def LoadSecretKey(self) -> bool:
        pass
    @abstractmethod
    def CheckSecretKey(self, key: str) -> bool:
        pass
    @abstractmethod
    def ValidatePassword(self, password: str) -> bool:
        pass