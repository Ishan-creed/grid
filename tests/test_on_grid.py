import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

@pytest.mark.parametrize("browser", ["chrome", "firefox", "edge"])
def test_on_grid(browser, selected_browser):
    if selected_browser and selected_browser.lower() != browser:
        pytest.skip(f"Skipping test for browser: {browser}")

    grid_url = "http://localhost:4444/wd/hub"
    
    if browser == "chrome":
        options = ChromeOptions()
    elif browser == "firefox":
        options = FirefoxOptions()
    elif browser == "edge":
        options = EdgeOptions()
    else:
        raise ValueError("Unsupported browser")

    # Remove `--headless` to run in visible mode
    # Add Docker-compatible options
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")  # Helps avoid rendering issues in Docker
    
    driver = webdriver.Remote(
        command_executor=grid_url,
        options=options
    )
    
    try:
        driver.get("https://google.com")
        assert "Google" in driver.title
    finally:
        driver.quit()
