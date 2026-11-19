# Level 2 – Toolshop Website Automation Testing

## 1. Project Overview

This project focuses on testing the Toolshop e-commerce application using Python and Playwright.

The objective is to perform automated functional testing on two versions of the application:

- **Reference Build:** https://practicesoftwaretesting.com
- **Bug Build:** https://with-bugs.practicesoftwaretesting.com

The same automated test suite is executed against both builds to identify differences in application behaviour and detect defects.

## 2. Technologies Used

- Python 3.13
- Playwright
- Pytest
- pytest-playwright
- pytest-html
- Chromium
- Visual Studio Code

## 3. Project Structure

```text
level2-toolshop/
│
├── bug-reports/
│   ├── BUG-001-incorrect-cart-line-total.md
│   ├── BUG-002-missing-add-to-cart-notification.md
│   ├── BUG-005-incorrect-contact-subject-options.md
│   ├── BUG-006-incorrect-contact-attachment-instructions.md
│   └── BUG-007-contact-subject-validation.md
│
├── screenshots/
│
├── tests/
│   ├── test_homepage.py
│   ├── test_product_listing.py
│   ├── test_sorting.py
│   ├── test_search.py
│   ├── test_product_details.py
│   ├── test_cart.py
│   └── test_contact.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## 4. Functionalities Tested

### 4.1 Homepage
- Verify homepage loads successfully.
- Verify important homepage elements are visible.

### 4.2 Product Listing
- Verify product cards are displayed.
- Check product listing functionality.

### 4.3 Product Sorting
- Sort products by name (A–Z).
- Sort products by name (Z–A).
- Sort products by price (Low–High).
- Sort products by price (High–Low).

### 4.4 Product Search
- Search for products by name.
- Verify relevant search results.

### 4.5 Product Details
- Verify product name.
- Verify product price.
- Verify product description.
- Verify Add to Cart button visibility and availability.

### 4.6 Shopping Cart
- Verify product is added to the cart.
- Verify product name, quantity and price.
- Verify cart line total.
- Verify cart total.
- Verify Add to Cart success notification.

### 4.7 Contact Form
- Verify all contact form fields are visible.
- Check empty form submission.
- Validate invalid email input.
- Check valid contact form submission.
- Verify subject dropdown options.
- Verify attachment instructions.
- Verify attachment file-type restriction.
- Explore PDF attachment submission.
- Verify subject selection and form submission.

## 5. Installation and Setup

Clone the repository:

```bash
git clone https://github.com/AyeshaCheulkar/PEPL-Software-Testing-Assignment
```

Navigate to the project folder:

```bash
cd PEPL-Software-Testing-Assignment/level2-toolshop
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright Chromium:

```bash
playwright install chromium
```

## 6. Running the Tests

### Run all tests against the Reference Build

```bash
pytest -v -s
```

### Run all tests against the Bug Build

```bash
pytest -v -s --shop-base-url=https://with-bugs.practicesoftwaretesting.com
```

### Run a specific test file

```bash
pytest tests/test_contact.py -v -s
```

### Run a specific test against the Bug Build

```bash
pytest tests/test_contact.py -v -s --shop-base-url=https://with-bugs.practicesoftwaretesting.com
```

## 7. Test Execution Results

The complete automated test suite contains 19 test cases and was executed against both application builds.

### 7.1 Overall Test Results

| Test Environment | Total Tests | Passed | Failed |
|---|---:|---:|---:|
| Reference Build | 19 | 19 | 0 |
| Bug Build | 19 | 13 | 6 |

**Reference Build:** All 19 test cases passed successfully.

**Bug Build:** 13 test cases passed and 6 test cases failed, exposing the identified application defects.

### 7.2 Feature-wise Test Results

| Functionality | Reference Build | Bug Build |
|---|---:|---:|
| Cart | 2 passed | 2 failed |
| Contact Form | 9 passed | 4 failed, 5 passed |
| Homepage | 1 passed | 1 passed |
| Product Details | 1 passed | 1 passed |
| Product Listing | 1 passed | 1 passed |
| Search | 1 passed | 1 passed |
| Sorting | 4 passed | 4 passed |
| **Total** | **19 passed** | **13 passed, 6 failed** |

### 7.3 Contact Form Test Results

| Test Environment | Passed | Failed |
|---|---:|---:|
| Reference Build | 9 | 0 |
| Bug Build | 5 | 4 |

The Bug Build produced four failures, exposing differences in subject dropdown options, attachment instructions, file input restrictions and subject validation.

**Note:** The valid submission and PDF attachment submission tests are exploratory tests that currently print the page result without asserting successful submission or PDF acceptance. Their passing pytest status does not independently establish successful form submission or PDF acceptance.

### 7.4 Identified Defects

| Bug ID | Description | Severity |
|---|---|---|
| BUG-001 | Incorrect cart line total | High |
| BUG-002 | Missing Add to Cart success notification | Medium |
| BUG-005 | Incorrect contact subject dropdown options | Medium |
| BUG-006 | Incorrect attachment instructions and missing file input restriction | Medium |
| BUG-007 | Contact form does not recognise the selected subject | Medium |

Detailed reproduction steps, expected results, actual results, impact and supporting evidence are documented in the `bug-reports/` directory.

## 8. Screenshots and Reports

- Screenshots of identified defects are stored in the `screenshots/` directory.
- Individual defect reports are maintained in the `bug-reports/` directory.
- Pytest HTML execution reports are generated as `report.html`.

## 9. Configuration

The base URL is configurable through the `--shop-base-url` command-line option.

The default URL points to the Reference Build.

The same test scripts can therefore be executed against both application versions without modifying the test code.

## 10. Conclusion

This project demonstrates functional automation testing using Python, Playwright and Pytest.

The test suite covers major Toolshop functionalities, including product listing, sorting, search, product details, shopping cart and contact form operations.

By executing the same automated tests against the Reference Build and Bug Build, differences in expected and actual application behaviour were identified and documented with supporting screenshots and defect reports.

The Reference Build passed all 19 test cases, while the Bug Build produced 6 failures that exposed 5 documented defects.

This project demonstrates the use of automated functional testing, test assertions, cross-build comparison, defect identification and evidence-based bug reporting.
