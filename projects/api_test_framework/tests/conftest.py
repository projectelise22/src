import pytest
from config.config import get_base_url

@pytest.fixture(scope="session")
def base_url():
    return get_base_url()