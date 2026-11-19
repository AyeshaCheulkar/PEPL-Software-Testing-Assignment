# PEPL – Testing / QA Technical Assignment

**Candidate:** Ayesha Cheulkar  
**Language:** Python  
**Testing Framework:** Pytest  

## 1. Project Overview

This repository contains my work for the PEPL Testing / QA Technical Assignment.

The completed work documented here covers API testing and UI automation testing using Python, Pytest and Playwright.

## 2. Repository Structure

```text
PEPL-Software-Testing-Assignment/
│
├── level1-restful-booker/
│   ├── tests/
│   ├── reports/
│   └── README.md
│
├── level2-toolshop/
│   ├── bug-reports/
│   ├── screenshots/
│   ├── tests/
│   ├── conftest.py
│   ├── pytest.ini
│   ├── requirements.txt
│   └── README.md
│
└── README.md
```

## 3. Level 1 – RESTful Booker API Testing

**Difficulty:** Easy

**Objective:** Test the RESTful Booker API and develop a reusable API testing framework.

**Application:** RESTful Booker  
Repository: https://github.com/mwinteringham/restful-booker

**Scope of Testing:**
- Authentication using token cookie and Basic authentication.
- Booking creation and retrieval.
- Booking update and partial update.
- Booking deletion.
- Invalid input and negative test scenarios.
- Response schema validation.
- Response-time verification.
- Complete booking lifecycle testing.

**How to Run:**

Navigate to the Level 1 folder:

```bash
cd level1-restful-booker
```

Run the test suite:

```bash
pytest -v
```

Refer to `level1-restful-booker/README.md` for setup instructions and additional details.

## 4. Level 2 – Toolshop Website Automation Testing

**Difficulty:** Hard

**Objective:** Identify defects in a bug-injected e-commerce application using automated browser testing.

**Technologies:**
- Python
- Playwright
- Pytest
- pytest-playwright
- pytest-html
- Chromium

**Application Builds:**

| Environment | URL |
|---|---|
| Reference Build | https://practicesoftwaretesting.com |
| Bug Build | https://with-bugs.practicesoftwaretesting.com |

**Scope of Testing:**
- Homepage and product listing.
- Product sorting.
- Product search.
- Product details.
- Shopping cart.
- Contact form validation and submission.

**How to Run:**

Navigate to the Level 2 folder:

```bash
cd level2-toolshop
```

Install dependencies:

```bash
pip install -r requirements.txt
playwright install chromium
```

Run tests against the Reference Build:

```bash
pytest -v -s
```

Run tests against the Bug Build:

```bash
pytest -v -s --shop-base-url=https://with-bugs.practicesoftwaretesting.com
```

**Test Execution Summary:**

| Environment | Passed | Failed |
|---|---:|---:|
| Reference Build | 19 | 0 |
| Bug Build | 13 | 6 |

Five defects were documented with reproduction steps and supporting screenshots.

Refer to `level2-toolshop/README.md` for detailed test results and bug reports.

## 5. Bug Reporting

For identified defects, individual bug reports include:

- Bug title and severity.
- Steps to reproduce.
- Expected result.
- Actual result.
- Supporting evidence.
- Why the defect matters.

A test exposing a defect is expected to fail or be marked as an expected failure with its corresponding bug ID.

## 6. General Notes

- Each completed level is maintained in a separate folder.
- Test execution instructions are provided in the respective level README files.
- The projects use automated testing to identify and document application defects.
- The repository is maintained using Git and GitHub.

## 7. Submission

**GitHub Repository:** Add your public repository URL here.