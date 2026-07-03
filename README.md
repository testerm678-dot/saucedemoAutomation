# Swag Labs Test Automation

End-to-end tests for [Swag Labs](https://www.saucedemo.com) using Playwright and pytest.

## What's in here?

- Login tests (standard user, locked-out user)
- Shopping cart operations
- Checkout flow
- Form validation tests

## Getting Started

### Prerequisites
- Python 3.8+
- Git

### Installation

1. Clone the repo
```bash
git clone <repository-url>
cd saucedemo
```

2. Create and activate virtual environment
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# Mac/Linux
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
playwright install
```

Done! Now You are ready to run tests.

## Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_login.py

# Run by marker
pytest -m login
pytest -m cart
pytest -m checkout

# Run with browser visible
pytest --headed

# Run specific browser
pytest --browser firefox
```

## Project Structure

```
saucedemo/
├── config/           # Settings & config
├── pages/            # Page Object Model
├── tests/            # Test files
├── pytest.ini        # Pytest config
└── requirements.txt  # Dependencies
```

## Configuration

Edit `config/settings.py` to change:
- Base URL (default: `https://www.saucedemo.com`)
- Test credentials
- Timeouts

Or use environment variables:
```bash
export BASE_URL=https://custom-url.com
export STANDARD_USER=your_user
```

## Test Results

Artifacts saved after each test run:
- Screenshots & videos in `test-results/`
- HTML report in `playwright-report/`

View report:
```bash
playwright show-report
```

## Issues?

Make sure:
- Python is installed (`python --version`)
- Virtual environment is activated (you'll see `(.venv)` in your prompt)
- Playwright browsers are installed (`playwright install`)
