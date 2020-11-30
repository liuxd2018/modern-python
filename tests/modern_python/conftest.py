"""Pakage-wide test fixtures."""
from unittest.mock import Mock

import pytest
from _pytest.config import Config
from pytest_mock import MockFixture


# register e2e marker using the pytest_configure hook
def pytest_configure(config: Config) -> None:
    """Pytest configuration hook."""
    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")


# this fixture in all the module under same directory
@pytest.fixture
def mock_requests_get(mocker: MockFixture) -> Mock:
    """Fixture for mocking requests get."""
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "Lorem ipsum dolor sit amet",
    }
    return mock
