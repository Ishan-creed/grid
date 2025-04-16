# tests/conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default=None, help="Specify browser: chrome, firefox, or edge"
    )

@pytest.fixture(scope="session")
def selected_browser(request):
    return request.config.getoption("--browser")
