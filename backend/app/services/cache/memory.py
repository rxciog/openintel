import time
from typing import Any, Optional
from .base import Cache

class InMemoryCache(Cache):
    def __init__(self):
        self._store: dict[str, tuple[Any, float]] = {}

    def get(self, key: str) -> Optional[Any]:
        entry = self._store.get(key)
        if not entry:
            return None
        
        value, expires_at = entry
        if expires_at < time.time():
            del self._store[key]
            return None
        
        return value
    
    def  set(self, key: str, value: Any, ttl: int) -> None:
        expires_at = time.time() + ttl
        self._store[key] = (value, expires_at)
