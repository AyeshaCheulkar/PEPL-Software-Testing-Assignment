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
git clone <your-github-repository-url>
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

### Contact Form Test Results

| Test Environment | Passed | Failed |
|---|---:|---:|
| Reference Build | 9 | 0 |
| Bug Build | 5 | 4 |

The Reference Build passed all nine Contact Form test cases.

The Bug Build produced four failures, exposing differences in subject dropdown options, attachment instructions, file input restrictions and subject validation.

**Note:** The valid submission and PDF attachment tests are exploratory tests that currently print the page result. Their passing pytest status does not independently establish successful form submission or PDF acceptance.

### Identified Defects

| Bug ID | Description | Severity |
|---|---|---|
| BUG-001 | Incorrect cart line total | High (provisional) |
| BUG-002 | Missing Add to Cart success notification | Medium (provisional) |
| BUG-005 | Unexpected errors in Contact subject dropdown | Medium (provisional) |
| BUG-006 | Missing file-type restriction on attachment input | Medium (provisional) |
| BUG-007 | Contact form does not recognise selected subject | Medium (provisional) |

Detailed reproduction steps, expected results, actual results and evidence are documented in the `bug-reports/` directory.

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

By executing the same tests against the Reference Build and Bug Build, differences in expected and actual application behaviour can be identified and documented with supporting evidence.