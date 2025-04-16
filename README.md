# Selenium Grid UI Test (GitHub Actions + Docker)

This project demonstrates how to run Python-based Selenium UI tests on **Chrome**, **Firefox**, and **Edge** browsers using:

**Selenium Grid (Dockerized)**  
**GitHub Actions CI/CD**  
**IntelliJ IDEA integration** (with .iml and Git VCS)

---

## Project Structure

```
.
├── .github/workflows/ui-grid.yml       # GitHub Actions workflow
├── .idea/selenium_ui.iml               # IntelliJ module file
├── requirements.txt                    # Python dependencies
├── tests/
│   └── test_on_grid.py                 # Selenium test file
```

---

## Quick Start

### Run Locally with Docker

# Start local Selenium Grid
docker-compose up -d

# Run tests (use chrome/firefox/edge)
pytest tests/test_on_grid.py --browser=chrome
```bash
docker-compose up -d   # (optional: if you're running local grid)
pytest tests/test_on_grid.py --browser=chrome
```

---

### Run in GitHub Actions

1. Push this repo to GitHub
2. GitHub Actions will:
   - Launch a browser container via Selenium Grid
   - Run the test inside the workflow (not headless)
   - Test `https://google.com` on all 3 browsers

You can monitor the Actions tab for real-time test logs.

---

## IntelliJ IDEA Integration

- `.iml` file is included
- Git VCS mapping is pre-configured via `.idea/vcs.xml`

To start:
1. Open the project in IntelliJ
2. Ensure Python SDK is set to 3.11+
3. You can run tests using the built-in terminal or PyCharm runner

---

## Customization

To come

