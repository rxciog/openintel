from abc import ABC, abstractmethod
from typing import Any, Optional

class Cache(ABC):
    @abstractmethod
    def get(self, key: str) -> Optional[Any]:
        pass
    @abstractmethod
    def set(self, key: str, value: Any, ttl: int) -> None:
        pass