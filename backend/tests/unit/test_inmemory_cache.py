import pytest
from unittest.mock import patch
from app.services.cache.memory import InMemoryCache

@pytest.fixture
def cache():
    return InMemoryCache()

def test_get_set_basic(cache):
    """Confirm basic storage and retrieval works."""
    cache.set("test_key", "test_value", ttl=10)
    assert cache.get("test_key") == "test_value"

def test_cache_miss(cache):
    """Confirm that non-existent keys return None."""
    assert cache.get("non_existent") is None

def test_expiration_logic(cache):
    """Verify that items 'disappear' only after TTL has passed."""
    # Use patch to 'freeze' and 'jump' through time
    with patch("time.time") as mock_time:
        # 1. Set initial time
        mock_time.return_value = 1000.0
        cache.set("expired_key", "some_data", ttl=5) # Expires at 1005.0

        # 2. Check halfway through (should be present)
        mock_time.return_value = 1002.0
        assert cache.get("expired_key") == "some_data"

        # 3. Check after expiration (should be None)
        mock_time.return_value = 1006.0
        assert cache.get("expired_key") is None
        
        # 4. Confirm it was actually purged from internal dict
        assert "expired_key" not in cache._store

def test_overwrite_key_updates_ttl(cache):
    """Confirm that setting an existing key resets its value and expiration."""
    with patch("time.time") as mock_time:
        mock_time.return_value = 1000.0
        cache.set("key", "val1", ttl=10) # Expires 1010
        
        mock_time.return_value = 1005.0
        cache.set("key", "val2", ttl=10) # New expiry 1015
        
        mock_time.return_value = 1012.0
        # If it didn't update, this would be None. Since it updated, it's val2.
        assert cache.get("key") == "val2"