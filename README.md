# PEPL – Testing / QA Technical Assignment

[![API Tests](https://github.com/AyeshaCheulkar/PEPL-Software-Testing-Assignment/actions/workflows/pytest.yml/badge.svg)](https://github.com/AyeshaCheulkar/PEPL-Software-Testing-Assignment/actions/workflows/pytest.yml)

**Candidate:** Ayesha Cheulkar  
**Language:** Python · **Frameworks:** Pytest, Playwright

This repository contains my work for the PEPL Testing / QA Technical Assignment. It includes two completed levels: API automation testing (Level 1) and UI automation testing with bug hunting (Level 2).

## Table of Contents

- [At a Glance](#at-a-glance)
- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Level 1 – Restful Booker API Testing](#level-1--restful-booker-api-testing)
- [Level 2 – Toolshop UI Automation Testing](#level-2--toolshop-ui-automation-testing)
- [Bug Reporting](#bug-reporting)
- [Notes](#notes)
- [Submission](#submission)

## At a Glance

| | Level 1 | Level 2 |
|---|---|---|
| **Focus** | API automation | UI automation and defect finding |
| **Difficulty** | Easy | Hard |
| **Application** | Restful Booker (run locally) | Practice Software Testing (reference and bug builds) |
| **Tools** | Pytest, Requests, jsonschema | Pytest, Playwright, pytest-html |
| **Result** | Full test suite with HTML report and CI | 19/19 passed on reference build; 6 failures on bug build |
| **Details** | Level 1 README | Level 2 README |

## Repository Structure

```text
PEPL-Software-Testing-Assignment/
├── .github/
│   └── workflows/
│       └── pytest.yml              # CI for Level 1
├── level1-restful-booker/
│   ├── schemas/
│   ├── tests/
│   ├── utils/
│   ├── reports/
│   ├── conftest.py
│   ├── pytest.ini
│   ├── requirements.txt
│   ├── test_plan.md
│   └── README.md
├── level2-toolshop/
│   ├── bug-reports/
│   ├── screenshots/
│   ├── tests/
│   ├── conftest.py
│   ├── pytest.ini
│   ├── requirements.txt
│   └── README.md
└── README.md
```

## Prerequisites

- Python 3.11 or higher
- Git
- Node.js and npm (Level 1 only, to run the Restful Booker API)

Using a virtual environment is recommended:

```bash
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

## Level 1 – Restful Booker API Testing

**Objective:** Test the [Restful Booker](https://github.com/mwinteringham/restful-booker) API and build a reusable API testing framework.

### Scope

- Authentication with token cookie and Basic auth
- Booking creation and retrieval
- Full (PUT) and partial (PATCH) updates
- Deletion and 404 verification
- Invalid input and negative scenarios
- Response schema validation
- Response-time verification
- Complete booking lifecycle

### How to Run

Start the Restful Booker API at `http://localhost:3001` (refer to the Level 1 README for setup instructions).

Then run:

```bash
cd level1-restful-booker
pip install -r requirements.txt
pytest -v
```

Setup details, HTML report generation, and the CI workflow are covered in `level1-restful-booker/README.md`. The full testing scope and strategy are documented in `level1-restful-booker/test_plan.md`.

## Level 2 – Toolshop UI Automation Testing

**Objective:** Identify defects in a bug-injected e-commerce application using automated browser tests.

**Technologies:** Python, Pytest, Playwright, pytest-playwright, pytest-html, Chromium

### Application Builds

| Build | URL |
|---|---|
| Reference (correct behaviour) | [https://practicesoftwaretesting.com](https://practicesoftwaretesting.com) |
| Bug build (injected defects) | [https://with-bugs.practicesoftwaretesting.com](https://with-bugs.practicesoftwaretesting.com) |

### Scope

- Homepage and product listing
- Product sorting
- Product search
- Product details
- Shopping cart
- Contact form validation and submission

### How to Run

Install the dependencies:

```bash
cd level2-toolshop
pip install -r requirements.txt
playwright install chromium
```

**Against the reference build:**

```bash
pytest -v -s
```

**Against the bug build:**

```bash
pytest -v -s --shop-base-url=https://with-bugs.practicesoftwaretesting.com
```

### Test Results

| Build | Passed | Failed |
|---|---:|---:|
| Reference | 19 | 0 |
| Bug | 13 | 6 |

The same automated test suite was executed against both builds. All 19 tests passed on the reference build, while 6 tests failed on the bug build, exposing differences in application behaviour.

These failures were investigated and documented in individual bug reports. Reproduction steps and screenshots are available in `level2-toolshop/bug-reports/` and `level2-toolshop/screenshots/`.

Refer to `level2-toolshop/README.md` for detailed test results and defect descriptions.

## Bug Reporting

Each identified defect has an individual report containing:

- Bug ID, title, and severity
- Steps to reproduce
- Expected result
- Actual result
- Supporting evidence (screenshots)
- Why the defect matters

A test that exposes a defect is expected to fail or be marked as an expected failure (`xfail`) with a reference to its bug ID. Incorrect application behaviour should not be treated as a successful test outcome.

## Notes

- Each level has its own folder, README, and dependencies.
- Run commands from inside the relevant level folder, as shown above.
- The repository is maintained using Git and GitHub.

## Submission

**GitHub Repository:** [PEPL-Software-Testing-Assignment](https://github.com/AyeshaCheulkar/PEPL-Software-Testing-Assignment)

**Author:** Ayesha Cheulkar  
[GitHub](https://github.com/AyeshaCheulkar) · [LinkedIn](https://www.linkedin.com/in/ayesha-cheulkar-6ba8ab249)