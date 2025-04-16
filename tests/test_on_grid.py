import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.mark.parametrize("browser", ["chrome", "firefox", "edge"])
def test_on_grid(browser):
    grid_url = "http://localhost:4444/wd/hub"
    if browser == "chrome":
        capabilities = DesiredCapabilities.CHROME.copy()
    elif browser == "firefox":
        capabilities = DesiredCapabilities.FIREFOX.copy()
    elif browser == "edge":
        capabilities = DesiredCapabilities.EDGE.copy()
    else:
        raise ValueError("Unsupported browser")
    
    driver = webdriver.Remote(command_executor=grid_url, desired_capabilities=capabilities)
    driver.get("https://google.com")
    assert "Google Domain" in driver.title
    driver.quit()
