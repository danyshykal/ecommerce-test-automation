# E-Commerce Website Test Automation

Automated UI tests for [SauceDemo](https://www.saucedemo.com), a demo e-commerce site, using **Python + Playwright + pytest** with the **Page Object Model**.

## What's covered
| Area | Tests |
|---|---|
| Login | valid login, wrong password, empty fields, locked user, logout |
| Inventory | product list, sort by price, sort by name |
| Cart | add item, remove item, cart contents |
| Checkout | full purchase flow + total check, form validation |

Manual test cases: [`docs/test_cases.csv`](docs/test_cases.csv)

## Project structure
```
pages/      # Page Objects (locators + actions per page)
tests/      # Test files + fixtures (conftest.py)
docs/       # Manual test cases, bug reports
reports/    # HTML report (generated)
```

## Run locally
```bash
python -m venv venv
venv\Scripts\activate          # Windows  (Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
playwright install chromium
pytest                          # headless
pytest --headed --slowmo 500    # watch the browser
pytest -m smoke                 # only smoke tests
```
Report: `reports/report.html`

## CI
GitHub Actions runs every test on each push (`.github/workflows/tests.yml`) and uploads the HTML report.
