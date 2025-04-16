import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Add this function to register the custom command line option
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default=None, help="Specify browser: chrome, firefox, or edge"
    )

# Fixture to obtain the selected browser from the CLI
@pytest.fixture(scope="session")
def selected_browser(request):
    return request.config.getoption("--browser")

# Parameterizing across multiple browsers
@pytest.mark.parametrize("browser", ["chrome", "firefox", "edge"])
def test_on_grid(browser, selected_browser):
    # If a specific browser is specified, skip the unmatched tests
    if selected_browser and selected_browser.lower() != browser:
        pytest.skip(f"Skipping test for browser: {browser}")

    grid_url = "http://localhost:4444/wd/hub"
    if browser == "chrome":
        capabilities = DesiredCapabilities.CHROME.copy()
    elif browser == "firefox":
        capabilities = DesiredCapabilities.FIREFOX.copy()
    elif browser == "edge":
        capabilities = DesiredCapabilities.EDGE.copy()
    else:
        raise ValueError("Unsupported browser")
    
    driver = webdriver.Remote(
        command_executor=grid_url,
        desired_capabilities=capabilities
    )
    driver.get("https://google.com")
    # Adjust assertion if necessary: generally Google title includes "Google"
    assert "Google" in driver.title
    driver.quit()
