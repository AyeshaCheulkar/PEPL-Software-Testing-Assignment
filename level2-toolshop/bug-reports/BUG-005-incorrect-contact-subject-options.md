# BUG-005: Unexpected Error Messages in Contact Subject Dropdown

**Severity:** Medium (provisional)  
**Module:** Contact Form  
**Environment:** Bug Build – https://with-bugs.practicesoftwaretesting.com  
**Browser:** Chromium  
**Status:** Open

## Description

The Subject dropdown on the Contact page displays unexpected error messages as selectable options instead of displaying only valid subject categories.

The dropdown contains the following unexpected options:

- Error 101: Subject not found
- Error 202: Translation error

These options are not present on the reference website.

## Steps to Reproduce

1. Open https://with-bugs.practicesoftwaretesting.com.
2. Navigate to the Contact page.
3. Locate the Subject dropdown.
4. Open the dropdown and inspect the available options.
5. Observe the unexpected error messages.

## Expected Result

The Subject dropdown should display only valid subject categories:

- Customer service
- Webmaster
- Return
- Payments
- Warranty
- Status of my order

No error messages should appear as selectable options.

## Actual Result

The Subject dropdown contains two unexpected options:

- Error 101: Subject not found
- Error 202: Translation error

## Evidence

- Screenshot: `contact-subject-dropdown-errors.png`
- Automated test: `test_contact_subject_options`
- Test result: FAILED on bug build because Error 101 was found.

The terminal accessibility snapshot also confirms the presence of Error 202.

## Impact

Users may select an invalid subject option when submitting the Contact Form. This could cause confusion or interfere with correct categorisation of their enquiries. The actual submission impact has not yet been verified.