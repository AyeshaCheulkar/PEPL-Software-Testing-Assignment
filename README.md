# Restful Booker API Automation Testing

![API Tests](https://github.com/AyeshaCheulkar/PEPL-Software-Testing-Assignment/actions/workflows/pytest.yml/badge.svg)

**PEPL Software Testing Assignment · Level 1 – API Automation Testing**

**Candidate:** Ayesha Cheulkar

An automated API testing framework for the [Restful Booker](https://github.com/mwinteringham/restful-booker) application, built using Python, Pytest and Requests. The framework supports local execution and continuous integration through GitHub Actions, with self-contained HTML test reports.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Running the Tests](#running-the-tests)
- [HTML Test Report](#html-test-report)
- [Test Coverage](#test-coverage)
- [Continuous Integration](#continuous-integration)
- [Troubleshooting](#troubleshooting)
- [Documentation](#documentation)
- [Author](#author)

## Features

- **Reusable API Client:** Centralises HTTP requests, URLs and session handling.
- **Test Data Builders:** Generate reusable booking payloads for test execution.
- **Pytest Fixtures:** Manage test setup, authentication and cleanup.
- **Parametrised Testing:** Validate multiple invalid-input scenarios.
- **JSON Schema Validation:** Verify API response structures and data types.
- **Configurable Base URL:** Supports a default URL and custom configuration through the `BASE_URL` environment variable.
- **Response-Time Validation:** Checks API response time against a two-second threshold.
- **HTML Reporting:** Generates self-contained HTML test reports.
- **Continuous Integration:** Automatically executes tests through GitHub Actions.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.11+ | Programming language |
| Pytest | Test automation framework |
| Requests | HTTP API communication |
| jsonschema | JSON response schema validation |
| pytest-html | HTML test reporting |
| Node.js and npm | Run the Restful Booker API |
| Git and GitHub | Version control and repository hosting |
| GitHub Actions | Continuous integration |

## Project Structure

```text
PEPL-Software-Testing-Assignment/
│
├── .github/
│   └── workflows/
│       └── pytest.yml
│
├── level1-restful-booker/
│   ├── schemas/
│   │   └── booking_schema.json
│   │
│   ├── tests/
│   │   ├── test_auth.py
│   │   ├── test_booking_create.py
│   │   ├── test_booking_read.py
│   │   ├── test_booking_update.py
│   │   ├── test_booking_delete.py
│   │   ├── test_booking_schema.py
│   │   ├── test_invalid_inputs.py
│   │   ├── test_configuration.py
│   │   ├── test_ping.py
│   │   ├── test_response_time.py
│   │   └── test_test_data.py
│   │
│   ├── utils/
│   │   ├── api_client.py
│   │   └── test_data.py
│   │
│   ├── reports/
│   ├── conftest.py
│   ├── pytest.ini
│   ├── requirements.txt
│   └── test_plan.md
│
├── .gitignore
└── README.md
```

## Quick Start

### Prerequisites

Install the following tools:

- Python 3.11 or higher
- Node.js and npm
- Git

### 1. Clone the Assignment Repository

```bash
git clone https://github.com/AyeshaCheulkar/PEPL-Software-Testing-Assignment.git
cd PEPL-Software-Testing-Assignment
```

### 2. Create a Virtual Environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Python Dependencies

From the assignment root directory:

```bash
pip install -r level1-restful-booker/requirements.txt
```

### 4. Download and Start the Restful Booker API

The Restful Booker application is maintained in a separate repository.

Clone it into the assignment root directory:

```bash
git clone https://github.com/mwinteringham/restful-booker.git
```

Navigate to the application directory:

```bash
cd restful-booker
```

Install its dependencies:

```bash
npm install
```

Start the API:

```bash
npm start
```

The API should be available at:

`http://localhost:3001`

Keep the API terminal running while executing the tests.

## Running the Tests

Open a separate terminal, activate your Python virtual environment and navigate to the testing directory:

```bash
cd level1-restful-booker
```

### Run the Complete Test Suite

```bash
python -m pytest -v
```

### Run a Specific Test File

```bash
python -m pytest tests/test_auth.py -v
```

### Run Tests Matching a Keyword

```bash
python -m pytest -v -k "delete"
```

## HTML Test Report

To generate a self-contained HTML report, run:

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

The report will be saved at:

`level1-restful-booker/reports/report.html`

Open the generated HTML file in a web browser to review test results, execution details and failures.

## Test Coverage

| Testing Area | Scenarios Covered |
|---|---|
| Authentication | Valid and invalid credentials, token-cookie authentication and Basic authentication |
| Booking Creation | Creating bookings using valid test data |
| Booking Retrieval | Retrieving existing bookings by ID |
| Booking Update | Full updates using PUT and partial updates using PATCH |
| Booking Deletion | Deleting bookings and verifying subsequent 404 responses |
| Negative Testing | Invalid booking IDs and negative input scenarios |
| Schema Validation | Validating API responses against JSON Schema |
| Configuration | Default and custom API base URL |
| Health Check | API ping endpoint |
| Response Time | Response time validation against a two-second threshold |
| Test Data | Test-data generation and reusable payloads |

## Continuous Integration

The project uses GitHub Actions for automated test execution.

The workflow is located at:

`.github/workflows/pytest.yml`

It runs automatically on every push and pull request to the `main` branch.

### Workflow Execution Steps

1. Checks out the assignment repository.
2. Downloads the Restful Booker application from its original repository.
3. Sets up Python and Node.js.
4. Installs Python and Node.js dependencies.
5. Starts the Restful Booker API.
6. Executes the Pytest test suite.
7. Generates and uploads the HTML test report as a workflow artifact.

Workflow execution results can be viewed under the **Actions** tab of the GitHub repository.

The HTML report can be downloaded from the artifacts section of a completed workflow run.

## Troubleshooting

| Problem | Possible Cause and Solution |
|---|---|
| Connection refused | The API is not running. Start it using `npm start`. |
| Port 3001 already in use | Stop the existing process using the port before restarting the API. |
| Pytest not found | Activate the virtual environment and install the Python dependencies. |
| PowerShell blocks virtual environment activation | Use `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` if permitted by your system. |
| Response-time test fails | Response time can vary by environment. Check API availability and repeat the measurement before investigating further. |
| HTML report is not generated | Check that `pytest-html` is installed and the `reports` directory exists. |

## Documentation

For more information about the testing scope, methodology, test scenarios, test environment, risks and entry/exit criteria, refer to:

[`level1-restful-booker/test_plan.md`](level1-restful-booker/test_plan.md)

## Repository

**GitHub:** [PEPL Software Testing Assignment](https://github.com/AyeshaCheulkar/PEPL-Software-Testing-Assignment)

## Author

**Ayesha Cheulkar**

- [GitHub Profile](https://github.com/AyeshaCheulkar)
- [LinkedIn Profile](https://www.linkedin.com/in/ayesha-cheulkar-6ba8ab249)