Test Plan: Restful Booker API Testing
Project: PEPL Software Testing Assignment Level: Level 1 – API Automation Testing Framework: Python, Pytest, Requests API under test: Restful Booker (http://localhost:3001) Author: Ayesha Cheulkar Version: 1.0
1. Introduction and Objective
This plan describes how the Restful Booker API is tested through automation. The goal is to verify its functionality, reliability and behaviour across authentication, booking operations, input validation, response structure, configuration and response time.
The framework is built to be reusable and maintainable, and to run the same way on a local Windows machine and in a GitHub Actions pipeline on Ubuntu.
2. Scope
2.1 In scope
Area
What is verified
Authentication
Valid and invalid credentials; token-cookie and Basic authentication
Booking creation
Bookings are created from valid test data and return the expected body
Booking retrieval
Existing bookings can be fetched by ID
Booking update
Full update with PUT; partial update with PATCH
Booking deletion
Deletion succeeds; a deleted booking then returns 404
Negative testing
Invalid booking IDs and invalid or incomplete input
Schema validation
Responses match the expected JSON structure and data types
Configuration
Default and custom base URL settings
Response time
Responses arrive within a two-second threshold
2.2 Out of scope
• UI testing, load or stress testing, and security penetration testing.
• Testing of the hosted public Restful Booker instance (only the local instance is used).
• Database-level verification.
3. Test Strategy
1.  Reusable API client: a single client class sends all HTTP requests, so URL, headers and authentication are handled in one place.
2.  Test-data builders: helper functions generate valid booking payloads and controlled invalid variants.
3.  Fixtures: Pytest fixtures handle setup (for example creating a booking or obtaining a token) and cleanup (deleting created bookings).
4.  Parametrised tests: one test body covers many invalid-input scenarios.
5.  Schema validation: jsonschema checks response structure, not just status codes.
6.  Test independence: each test creates and removes its own data, so tests can run in any order.
7.  Reporting: pytest-html produces a self-contained report for every run.
4. Test Scenarios
ID
Area
Scenario
Expected result
AUTH-01
Authentication
Request a token with valid credentials
Token is returned
AUTH-02
Authentication
Request a token with invalid credentials
No token; "Bad credentials" reason returned
AUTH-03
Authentication
Update a booking using Basic authentication
Request is accepted
AUTH-04
Authentication
Update or delete a booking with no authentication
Request is rejected (403)
BK-01
Create
Create a booking with valid data
Booking ID returned; body matches input
BK-02
Retrieve
Get an existing booking by ID
200; fields match the created booking
BK-03
Update (PUT)
Replace all fields of a booking
200; all fields updated
BK-04
Update (PATCH)
Change one or two fields only
200; only those fields change
BK-05
Delete
Delete an existing booking
Deletion confirmed
BK-06
Delete
Get the booking after deletion
404 Not Found
NEG-01
Negative
Get a booking with a non-existent ID
404 Not Found
NEG-02
Negative
Create a booking with missing, empty or wrongly typed fields (parametrised)
Request rejected or error returned
SCH-01
Schema
Validate create, retrieve and update responses
Responses match the JSON schema
CFG-01
Configuration
Run with the default base URL
Tests target http://localhost:3001
CFG-02
Configuration
Run with a custom base URL
Tests target the custom URL
PERF-01
Response time
Measure key endpoints
Each responds in under 2 seconds
Exact status codes follow the documented behaviour of the Restful Booker API and are confirmed during test implementation.
5. Test Environment and Tools
Component
Technology
Language
Python
Test framework
Pytest
HTTP library
Requests
Schema validation
jsonschema
API under test
Restful Booker (runs on Node.js)
Editor
Visual Studio Code
Version control
Git and GitHub
CI
GitHub Actions
Reporting
pytest-html
Execution environments: Windows (local) and Ubuntu Linux (GitHub Actions).
6. Entry and Exit Criteria
Entry criteria
• The Restful Booker application is installed and running.
• Python and all dependencies are installed.
• The base URL is configured correctly.
• Test files and test data are available.
Exit criteria
• All planned automated tests have been executed.
• No unexpected failures remain; any known failures are documented.
• Response structures are validated against schemas.
• The HTML report is generated.
• The GitHub Actions workflow completes successfully.
7. Risks and Mitigation
Risk
Impact
Mitigation
API is unavailable or the network is interrupted
Tests fail for non-functional reasons
Confirm the API is reachable before the run; in CI, wait for the service to start before testing
Response times vary between machines
False failures on the two-second check
Keep the threshold configurable and re-run before logging a defect
API behaviour changes after an update
Tests become outdated
Pin the API version used and review tests on each update
Shared or leftover test data
Tests interfere with each other
Use fixtures that create and delete data per test
Dependency on external application and packages
Setup failures
Record dependencies in requirements.txt
8. Test Execution
Run from the level1-restful-booker directory.
Run all tests:
python -m pytest -v
Run all tests and generate an HTML report:
python -m pytest -v --html=reports/report.html --self-contained-html
Continuous integration: the GitHub Actions workflow downloads and starts Restful Booker, installs dependencies, runs the suite, and uploads the HTML report as a workflow artifact.
9. Deliverables
• Automated test suite and reusable API client
• Test-data builders and JSON schemas
• HTML test report
• GitHub Actions workflow file
• This test plan
10. Expected Outcome
A reusable API automation framework that validates the main Restful Booker operations, authentication mechanisms, negative scenarios, response schemas and the response-time threshold, and that runs successfully both locally and through GitHub Actions.